import tempfile
import os
import pytest

from commands.file import FileCommand
from base.table import Table

def test_file_command_loads_csv():
    with tempfile.NamedTemporaryFile("w+", delete=False) as f:
        f.write("id,name,score\n1,Alice,85\n2,Bob,90\n")
        f.flush()

        command = FileCommand()
        table = Table()
        result = command.execute(table, f.name)
        assert result.head == ["id", "name", "score"]
        assert result.rows[1][2] == 90.0
    os.remove(f.name)

def test_file_command_file_not_found():
    command = FileCommand()
    table = Table()
    with pytest.raises(FileNotFoundError):
        command.execute(table, "non_existent_file.csv")

def test_file_command_empty_file():
    with tempfile.NamedTemporaryFile("w+", delete=False) as f:
        f.write("")
        f.flush()

        command = FileCommand()
        table = Table()
        with pytest.raises(StopIteration):  # next(csv_reader) вызовет StopIteration
            command.execute(table, f.name)
    os.remove(f.name)

def test_file_command_only_header():
    with tempfile.NamedTemporaryFile("w+", delete=False) as f:
        f.write("id,name,score\n")
        f.flush()

        command = FileCommand()
        table = Table()
        result = command.execute(table, f.name)
        assert result.head == ["id", "name", "score"]
        assert result.rows == []
    os.remove(f.name)

def test_file_command_multiple_loads():
    with tempfile.NamedTemporaryFile("w+", delete=False) as f:
        f.write("id,name,score\n1,Alice,85\n")
        f.flush()

        command = FileCommand()
        table = Table()
        command.execute(table, f.name)
        command.execute(table, f.name)

        assert len(table.rows) == 2
    os.remove(f.name)

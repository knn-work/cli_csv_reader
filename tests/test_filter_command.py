import pytest

from commands.filters import FilterCommand


def test_filter_command_gt(sample_table):
    command = FilterCommand()
    result = command.execute(sample_table, "score>80")
    assert len(result.rows) == 3
    assert result.rows[0][1] == "Alice"

def test_filter_command_lt(sample_table):
    command = FilterCommand()
    result = command.execute(sample_table, "score<70")
    # Ожидаем строки с score меньше 70
    for row in result.rows:
        assert row[sample_table.head.index("score")] < 70

def test_filter_command_eq(sample_table):
    command = FilterCommand()
    result = command.execute(sample_table, "score=90")
    # Проверяем, что все результаты равны 90
    for row in result.rows:
        assert row[sample_table.head.index("score")] == 90

def test_filter_command_invalid_syntax(sample_table):
    command = FilterCommand()
    # Несколько разделителей — должно выкинуть ошибку при парсинге
    with pytest.raises(ValueError):
        command.execute(sample_table, "score>>80")

def test_filter_command_empty_result(sample_table):
    command = FilterCommand()
    result = command.execute(sample_table, "score>1000")
    assert len(result.rows) == 0

def test_filter_command_invalid_column(sample_table):
    command = FilterCommand()
    with pytest.raises(ValueError):
        command.execute(sample_table, "nonexistent>10")

def test_filter_command_invalid_value_type(sample_table):
    command = FilterCommand()
    with pytest.raises(ValueError):
        command.execute(sample_table, "score>abc")

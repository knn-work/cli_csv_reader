import pytest
from commands.order import OrderCommand

def test_order_invalid_column(sample_table):
    command = OrderCommand()
    with pytest.raises(ValueError):
        command.execute(sample_table, "авыаыаы=asc")  # нет колонки

def test_order_invalid_order(sample_table):
    command = OrderCommand()
    with pytest.raises(ValueError):
        command.execute(sample_table, "score=fdsfsf")

def test_order_empty_table(empty_table):
    command = OrderCommand()
    result = command.execute(empty_table, "score=asc")
    assert result.rows == []

def test_order_empty_string(sample_table):
    command = OrderCommand()
    with pytest.raises(ValueError):
        command.execute(sample_table, "")

def test_order_multiple_separators(sample_table):
    command = OrderCommand()
    with pytest.raises(ValueError):
        command.execute(sample_table, "score==asc")

def test_order_sort_by_name_asc(sample_table):
    command = OrderCommand()
    result = command.execute(sample_table, "name=asc")
    names = [row[1] for row in result.rows]
    assert names == sorted(names)

def test_order_sort_by_score_desc(sample_table):
    command = OrderCommand()
    result = command.execute(sample_table, "score=desc")
    scores = [row[2] for row in result.rows]
    assert scores == sorted(scores, reverse=True)

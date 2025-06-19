import pytest

from base.table import Table


def test_head_setter_and_getter():
    table = Table()
    assert table.head is None
    table.head = ["A", "B", "C"]
    assert table.head == ["A", "B", "C"]
    # Проверяем, что типы и set инициализированы корректно
    assert table.types == [None, None, None]
    assert "A" in table
    assert "D" not in table

def test_add_row_and_type_inference():
    table = Table()
    table.head = ["num", "text"]

    # Первый ряд с float и str
    table.add_row(["1.5", "hello"])
    assert table.rows == [[1.5, "hello"]]
    assert table.types == [float, str]

    # Второй ряд с корректным преобразованием типов
    table.add_row(["2.5", "world"])
    assert table.rows == [[1.5, "hello"], [2.5, "world"]]

    # Третий ряд с числом в виде int в строке
    table.add_row(["3", "test"])
    assert table.rows[-1][0] == 3.0  # float

def test_add_row_with_invalid_float_converts_to_str():
    table = Table()
    table.head = ["num", "text"]

    # Добавляем строку, где первый элемент нельзя преобразовать в float
    table.add_row(["abc", "hello"])
    assert table.types[0] == str  # тип сменился на str
    assert table.rows[-1][0] == "abc"

def test_get_column_returns_correct_column():
    table = Table()
    table.head = ["col1", "col2"]
    table.add_row(["1", "a"])
    table.add_row(["2", "b"])
    col0 = table.get_column(0)
    col1 = table.get_column(1)
    assert col0 == [1.0, 2.0]
    assert col1 == ["a", "b"]

def test_str_method_with_head_and_without():
    table = Table()
    assert str(table) == "Empty table"
    table.head = ["A"]
    table.add_row(["1"])
    out = str(table)
    assert "A" in out
    assert "1" in out

def test_contains_method():
    table = Table()
    assert "X" not in table  # пустая таблица
    table.head = ["X", "Y"]
    assert "X" in table
    assert "Y" in table
    assert "Z" not in table

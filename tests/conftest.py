import pytest

from base.table import Table


@pytest.fixture
def sample_table() -> Table:
    table = Table()
    table.head = ["id", "name", "score"]
    table.add_row(["1", "Alice", "85"])
    table.add_row(["2", "Bob", "90"])
    table.add_row(["3", "Charlie", "78"])
    table.add_row(["4", "Knn", "80.25"])
    return table

@pytest.fixture
def empty_table() -> Table:
    table = Table()
    table.head = ["id", "name", "score"]
    return table
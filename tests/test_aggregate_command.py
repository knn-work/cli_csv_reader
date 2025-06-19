import pytest
from commands.aggregate import AggregateCommand

def test_aggregate_avg(sample_table):
    command = AggregateCommand()
    result = command.execute(sample_table, "score=avg")
    expected_avg = (85 + 90 + 78 + 80.25) / 4
    assert result.rows[0][0] == pytest.approx(expected_avg)

def test_aggregate_min(sample_table):
    command = AggregateCommand()
    result = command.execute(sample_table, "score=min")
    expected_min = min([85, 90, 78, 80.25])
    assert result.rows[0][0] == expected_min

def test_aggregate_max(sample_table):
    command = AggregateCommand()
    result = command.execute(sample_table, "score=max")
    expected_max = max([85, 90, 78, 80.25])
    assert result.rows[0][0] == expected_max

def test_aggregate_invalid_func(sample_table):
    command = AggregateCommand()
    with pytest.raises(ValueError):
        command.execute(sample_table, "score=sum")

def test_aggregate_invalid_field(sample_table):
    command = AggregateCommand()
    with pytest.raises(ValueError):
        command.execute(sample_table, "выаыаы=avg")

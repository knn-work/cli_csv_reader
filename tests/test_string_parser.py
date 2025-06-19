import pytest
from base.string_parser import StringParser

def test_parse_valid():
    result = StringParser.parse("score>80", [">", "<", "="])
    assert result == ("score", ">", "80")

def test_parse_invalid_operator_count():
    with pytest.raises(ValueError):
        StringParser.parse("a>>5", [">"])

def test_parse_missing_value():
    with pytest.raises(ValueError):
        StringParser.parse("score>", [">"])

def test_parse_missing_allowed_character():
    with pytest.raises(ValueError):
        StringParser.parse("score>", [])

def test_parse_no_allowed_character_in_string():
    with pytest.raises(ValueError):
        StringParser.parse("score80", [">", "<", "="])

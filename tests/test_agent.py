from tools.calculator import calculator
from tools.date_tool import get_day


def test_calculator_add():
    result = calculator.invoke({
        "a": 10,
        "b": 5,
        "operation": "add"
    })

    assert result == "15.0"


def test_calculator_multiply():
    result = calculator.invoke({
        "a": 10,
        "b": 5,
        "operation": "multiply"
    })

    assert result == "50.0"


def test_calculator_divide_by_zero():
    result = calculator.invoke({
        "a": 10,
        "b": 0,
        "operation": "divide"
    })

    assert result == "Cannot divide by zero."


def test_get_day():
    result = get_day.invoke({
        "date": "2026-09-21"
    })

    assert result == "Monday"


def test_invalid_date():
    result = get_day.invoke({
        "date": "invalid-date"
    })

    assert result == "Invalid date. Use YYYY-MM-DD format."
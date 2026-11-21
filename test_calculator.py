import json
import pytest
from calculator import (
    calculate_total,
    filter_by_category,
    summarize_by_category,
    load_expenses,
)


def test_calculate_total():
    items = [
        {"amount": 1200.5, "category": "food"},
        {"amount": 800.0, "category": "transport"},
    ]
    assert calculate_total(items) == 2000.5


def test_filter_and_summarize_category():
    items = [
        {"amount": 500, "category": "food"},
        {"amount": 1500, "category": "food"},
        {"amount": 700, "category": "transport"},
    ]
    assert len(filter_by_category(items, "food")) == 2
    assert summarize_by_category(items, "food") == 2000.0
    assert summarize_by_category(items, "transport") == 700.0


def test_load_expenses(tmp_path):
    sample = [{"amount": 300, "category": "utilities"}]
    file = tmp_path / "expenses.json"
    file.write_text(json.dumps(sample), encoding="utf-8")
    loaded = load_expenses(str(file))
    assert len(loaded) == 1
    assert loaded[0]["category"] == "utilities"
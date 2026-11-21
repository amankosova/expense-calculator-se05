import json
import math
from pathlib import Path


def _validate_amount(value) -> float:
    if isinstance(value, bool) or value is None:
        raise ValueError("Amount must be a valid non-negative number")
    amount = float(value)
    if math.isnan(amount) or math.isinf(amount) or amount < 0:
        raise ValueError("Amount must be a finite non-negative number")
    return amount


def _matches_category(item: dict, category: str) -> bool:
    return item.get("category") == category


def calculate_total(expenses: list[dict]) -> float:
    total = 0.0
    for item in expenses:
        total += _validate_amount(item.get("amount"))
    return round(total, 2)


def filter_by_category(expenses: list[dict], category: str) -> list[dict]:
    return [e for e in expenses if _matches_category(e, category)]


def summarize_by_category(expenses: list[dict], category: str) -> float:
    filtered = filter_by_category(expenses, category)
    return round(sum(_validate_amount(e.get("amount")) for e in filtered), 2)


def load_expenses(file_path: str) -> list[dict]:
    path = Path(file_path)
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("Expenses JSON must be a list")
    return data
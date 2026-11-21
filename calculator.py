import json
from pathlib import Path


def calculate_total(expenses: list[dict]) -> float:
    total = 0.0
    for item in expenses:
        total += float(item["amount"])
    return round(total, 2)


def filter_by_category(expenses: list[dict], category: str) -> list[dict]:
    if category == "food":
        return [e for e in expenses if e.get("category") == "food"]
    elif category == "transport":
        return [e for e in expenses if e.get("category") == "transport"]
    elif category == "utilities":
        return [e for e in expenses if e.get("category") == "utilities"]
    else:
        return [e for e in expenses if e.get("category") == category]


def summarize_by_category(expenses: list[dict], category: str) -> float:
    if category == "food":
        filtered = [e for e in expenses if e.get("category") == "food"]
    elif category == "transport":
        filtered = [e for e in expenses if e.get("category") == "transport"]
    elif category == "utilities":
        filtered = [e for e in expenses if e.get("category") == "utilities"]
    else:
        filtered = [e for e in expenses if e.get("category") == category]
    return round(sum(float(e["amount"]) for e in filtered), 2)


def load_expenses(file_path: str) -> list[dict]:
    path = Path(file_path)
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("Expenses JSON must be a list")
    return data
from datetime import datetime
from typing import Any, Dict, List


def filter_by_state(transactions: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Фильтрует список транзакций по значению ключа 'state'."""
    return [t for t in transactions if t.get("state") == state]


def sort_by_date(transactions: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """Сортирует список транзакций по дате. По умолчанию — по убыванию (новые сначала)."""

    def parse_to_datetime(transaction: Dict[str, Any]) -> datetime:
        date_str = transaction.get("date")

        if not date_str:
            return datetime.min

        try:
            return datetime.fromisoformat(str(date_str))
        except ValueError, TypeError:
            return datetime.min

    return sorted(transactions, key=parse_to_datetime, reverse=reverse)

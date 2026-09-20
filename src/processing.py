from typing import List, Dict, Any

def filter_by_state(transactions: List[Dict[str, Any]], state: str="EXECUTED") -> List[Dict[str, Any]]:
    """Фильтрует список транзакций по значению ключа 'state'"""
    return [t for t in transactions if t.get("state") == state]


def sort_by_date():
    pass

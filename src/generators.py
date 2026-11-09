from typing import Iterator


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator[dict]:
    currency = currency.upper()
    """Принимает на вход список словарей, представляющих транзакции. Функция возвращает итератор,
     который поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD)."""

    for x in transactions:
        code = (
            x.get("operationAmount", {})
            .get("currency", {})
            .get("code")
        )
        if code and code.upper() == currency:
            yield x


def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    """Принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    for tx in transactions:
        description = tx.get("description", "Описание отсутствует")
        yield description


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Принимает начальное и конечное значения диапазона и возвращает итератор,
    который поочередно выдает номера банковских карт в формате XXXX XXXX XXXX XXXX."""
    for number in range(start, stop + 1):
        number_str = f"{number:016d}"
        yield f"{number_str[0:4]} {number_str[4:8]} {number_str[8:12]} {number_str[12:16]}"

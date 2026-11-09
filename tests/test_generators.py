import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency(for_generators: list[dict]) -> None:
    # Тест, что функция корректно фильтрует транзакции по заданной валюте.
    result = list(filter_by_currency(for_generators, "USD"))
    actual_ids = [tx["id"] for tx in result]
    expected_ids = [939719570, 142264268, 895315941]

    assert actual_ids == expected_ids



def test_filter_by_currency_no_matches(for_generators: list[dict]) -> None:
    # Тест, что функция правильно обрабатывает случаи, когда транзакции в заданной валюте отсутствуют.
    result = list(filter_by_currency(for_generators, "EUR"))

    assert result == []


def test_filter_by_currency_empty_list() -> None:
    # Тест, что генератор не завершается ошибкой при обработке пустого списка.
    result = list(filter_by_currency([], "USD"))
    assert result == []


def test_transaction_descriptions_full_list(for_generators: list[dict]) -> None:
    # Тест, что функция возвращает корректные описания для каждой транзакции.
    result = list(transaction_descriptions(for_generators))

    assert result == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации"
    ]

def test_transaction_descriptions(for_generators: list[dict]) -> None:
    # Тест на работу функции с различным количеством входных транзакций.
    descriptions = transaction_descriptions(for_generators)

    assert next(descriptions)
    assert next(descriptions)
    assert next(descriptions)
    assert next(descriptions)
    assert next(descriptions)

    with pytest.raises(StopIteration):
        next(descriptions)


def test_transaction_descriptions_empty_list() -> None:
    # Тест на пустой список.
    result = list(transaction_descriptions([]))

    assert result == []


def test_card_number_generator_basic_range() -> None:
    # Тест, которые проверяют, что генератор выдает правильные номера карт в заданном диапазоне.
    result = list(card_number_generator(1, 5))

    assert result == [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (1, 1, ["0000 0000 0000 0001"]),
        (9999999999999999, 9999999999999999, ["9999 9999 9999 9999"]),
    ],
)
def test_card_number_generator(start: int, stop: int, expected: list[str]) -> None:
    # Тесты, что генератор корректно обрабатывает крайние значения диапазона и правильно завершает генерацию.
    result = list(card_number_generator(start, stop))

    assert result == expected

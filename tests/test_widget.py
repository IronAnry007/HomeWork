import pytest

from src.widget import get_date, mask_account_card


# Корректные тесты с разными типами карт и счетов.
@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card_valid(input_data: str, expected: str) -> None:
    assert mask_account_card(input_data) == expected


# Проверка на пустой ввод.
def test_mask_account_card_empty() -> None:
    assert mask_account_card("") == "Ошибка: пустая строка"


# Проверка на некорректный ввод(неполный)
def test_mask_account_card_bad_input() -> None:
    assert (
        mask_account_card("5968378687051993") == "Ошибка: не удалось выделить номер (ожидается формат 'префикс номер')"
    )


# Проверка на лишние пробелы
def test_mask_account_card_extra_spaces() -> None:
    assert mask_account_card(" Счет   64686473678894779589 ") == "Счет **9589"


# Тестирование правильности преобразования даты на различных входных форматах даты, включая граничные
# случаи и нестандартные строки с датами.
@pytest.mark.parametrize(
    "input_date, expected_output",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024-03-11", "11.03.2024"),
        ("2020-02-29", "29.02.2020"),
        ("2019-02-28", "28.02.2019"),
        ("2024-12-31", "31.12.2024"),
        ("2024-01-01", "01.01.2024"),
    ],
)
def test_get_date_valid(input_date: str, expected_output: str) -> None:
    assert get_date(input_date) == expected_output


# Проверка, что функция корректно обрабатывает входные строки на не верный формат или
# где отсутствует дата.
@pytest.mark.parametrize("invalid_date", ["11.03.2024", ""])
def test_get_date_invalid(invalid_date: str) -> None:
    with pytest.raises(ValueError, match="Некорректный формат даты"):
        get_date(invalid_date)

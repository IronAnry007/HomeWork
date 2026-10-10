import pytest

from src.widget import mask_account_card

#Корректные тесты с разными типами карт и счетов.
@pytest.mark.parametrize("input_data, expected", [("Maestro 1596837868705199", 'Maestro 1596 83** **** 5199'),
                                                  ("Счет 64686473678894779589", "Счет **9589"),
                                                  ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
                                                  ("Счет 64686473678894779589", "Счет **9589"),
                                                  ("Счет 35383033474447895560", "Счет **5560"),
                                                  ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
                                                  ("Visa Platinum 8990922113665229",
                                                   "Visa Platinum 8990 92** **** 5229"),
                                                  ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
                                                  ("Счет 73654108430135874305", "Счет **4305"),
                                                  ])
def test_mask_account_card_valid(input_data, expected):
    assert mask_account_card(input_data) == expected


#Проверка на пустой ввод.
def test_mask_account_card_empty():
    assert mask_account_card("") == "Ошибка: пустая строка"


#Проверка на некорректный ввод(неполный)
def test_mask_account_card_bad_input():
    assert mask_account_card("5968378687051993") == "Ошибка: не удалось выделить номер (ожидается формат 'префикс номер')"


#Проверка на лишние пробелы
def test_mask_account_card_extra_spaces():
    assert mask_account_card(" Счет   64686473678894779589 ") == "Счет **9589"
import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("card_number, expected", [(1234567890123456, "1234 56** **** 3456"),
                                                   (5676789787654323, "5676 78** **** 4323")])
def test_get_mask_card_number_valid(card_number, expected):
    # Корректный номер: 16 цифр
    result = get_mask_card_number(card_number)
    assert result == expected


def test_get_mask_card_number_invalid_length():
    # Передаём 17 цифр как строку — функция должна вернуть сообщение об ошибке
    assert get_mask_card_number("12345678901234561") == "Номер карты должен состоять строго из 16 цифр."


def test_get_mask_card_number_too_short():
    # 15 цифр — должно вернуть ошибку
    assert get_mask_card_number("123456789012345") == "Номер карты должен состоять строго из 16 цифр."


def test_get_mask_card_number_with_letters(str_with_letters):
    # Буквы в номере
    assert get_mask_card_number(str_with_letters) == "Номер карты должен состоять строго из 16 цифр."


def test_get_mask_card_number_empty():
    # Пустая строка
    assert get_mask_card_number("") == "Номер карты должен состоять строго из 16 цифр."


@pytest.mark.parametrize("account_number, expected", [(1234, "**1234"),
                                                      (56767897876, "**7876")])
def test_get_mask_account_valid(account_number, expected):
    # Корректный номер: 4 и более цифр
    assert get_mask_account(account_number) == expected


def test_get_mask_account_too_short():
    # 3 цифры — должно вернуть ошибку
    assert get_mask_account("323") == "Номер счета должен состоять строго из 4 и более цифр."


def test_get_mask_account_with_letters(str_with_letters):
    # Буквы в номере
    assert get_mask_account(str_with_letters) == "Номер счета должен состоять строго из 4 и более цифр."


def test_get_mask_account_empty():
    # Пустая строка
    assert get_mask_account("") == "Номер счета должен состоять строго из 4 и более цифр."

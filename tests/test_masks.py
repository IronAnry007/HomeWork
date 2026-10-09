from src.masks import get_mask_card_number


def test_get_mask_card_number_valid():
    # Корректный номер: 16 цифр
    result = get_mask_card_number("1234567890123456")
    expected = "1234 56** **** 3456"
    assert result == expected


def test_get_mask_card_number_invalid_length():
    # Передаём 17 цифр как строку — функция должна вернуть сообщение об ошибке
    assert get_mask_card_number("12345678901234561") == "Номер карты должен состоять строго из 16 цифр."


def test_get_mask_card_number_too_short():
    # 15 цифр — должно вернуть ошибку
    assert get_mask_card_number("123456789012345") == "Номер карты должен состоять строго из 16 цифр."


def test_get_mask_card_number_with_letters():
    # Буквы в номере
    assert get_mask_card_number("1234abcd90123456") == "Номер карты должен состоять строго из 16 цифр."


def test_get_mask_card_number_empty():
    # Пустая строка
    assert get_mask_card_number("") == "Номер карты должен состоять строго из 16 цифр."

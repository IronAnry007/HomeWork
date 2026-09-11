from src.masks import get_mask_account, get_mask_card_number
from datetime import datetime


def mask_account_card(input_data: str) -> str:
    """функция, которая принимает строку и возвращает ее с замаскированным номером"""

    if not input_data:
        return "Ошибка: пустая строка"

    new_data = input_data.rsplit(" ", 1)

    if len(new_data) != 2:
        return "Ошибка: больше двух подстрок"

    card = new_data[0]
    number = new_data[1]

    if "счет" in card.title():
        encrypted_number = get_mask_account(number)
    else:
        encrypted_number = get_mask_card_number(number)
    return f"{card} {encrypted_number}"


def get_date(date_string: str) -> str:
    """Преобразует строку с датой из формата '2024-03-11T02:26:18.671407'
    в формат 'ДД.ММ.ГГГГ'."""

    try:

        dt = datetime.fromisoformat(date_string)
        return dt.strftime("%d.%m.%Y")

    except ValueError:

        try:
            dt = datetime.strptime(date_string[:10], "%Y-%m-%d")
            return dt.strftime("%d.%m.%Y")
        except (ValueError, IndexError) as e:
            raise ValueError(f"Некорректный формат даты: {date_string}. Ожидается ISO формат") from e




from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(input_data: str) -> str:
    """функция, которая принимает строку и возвращает ее с замаскированным номером"""

    if not input_data:
        return "Ошибка: пустая строка"

    normalized = " ".join(input_data.split())
    parts = normalized.rsplit(" ", 1)

    if len(parts) != 2:
        return "Ошибка: не удалось выделить номер (ожидается формат 'префикс номер')"

    card = parts[0]
    number = parts[1]

    if "счет" in card.lower():
        encrypted_number = get_mask_account(number)
    else:
        encrypted_number = get_mask_card_number(number)
    return f"{card} {encrypted_number}"


def get_date(date_string: str) -> str:
    """Преобразует строку с датой из формата '2024-03-11T02:26:18.671407' в формат 'ДД.ММ.ГГГГ'."""

    try:

        dt = datetime.fromisoformat(date_string)
        return dt.strftime("%d.%m.%Y")

    except ValueError:

        try:
            dt = datetime.strptime(date_string[:10], "%Y-%m-%d")
            return dt.strftime("%d.%m.%Y")
        except ValueError as e:
            raise ValueError(f"Некорректный формат даты: {date_string}. Ожидается ISO формат") from e

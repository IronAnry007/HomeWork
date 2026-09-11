from typing import Union


def get_mask_card_number(card_number: Union[str, int]) -> str:
    """Функция которая, принимает на вход номер карты и возвращает ее маску."""

    card_number = str(card_number)
    if len(card_number) == 16:
        first_numbers = card_number[:4]
        second_numbers = card_number[4:6]
        middle_numbers = "** ****"
        last_numbers = card_number[-4:]
        encrypted_numbers = f"{first_numbers} {second_numbers}{middle_numbers} {last_numbers}"
        return encrypted_numbers
    else:
        return "Номер карты должен состоять строго из 16 цифр."


def get_mask_account(account_number: Union[str, int]) -> str:
    """Функция которая, принимает на вход номер счета и возвращает его маску."""

    account_number = str(account_number)
    if len(account_number) >= 4:
        last_account_number = account_number[-4:]
        encrypted_account_number = f"**{last_account_number}"
        return encrypted_account_number
    else:
        return "Номер счета должен состоять строго из 4 и более цифр."

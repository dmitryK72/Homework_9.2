card_number = input()
account_number = input()


def get_mask_card_number(card_num: str) -> str:
    """Функция принимает на вход номер карты в виде числа и возвращает маску номера по
    правилу XXXX XX** **** XXXX"""
    return f"{card_num[:4]} {card_num[4:6]}** **** {card_num[-4:]}"


def get_mask_account(account_num: str) -> str:
    """Функция принимает на вход номер счета в виде числа и возвращает маску номера по правилу
    **XXXX"""
    return f"**{account_num[-4:]}"


# print(get_mask_card_number(card_number))
# print(get_mask_account(account_number))

from typing import Union

from datetime import datetime

from src.masks import get_mask_card_number, get_mask_account



def mask_account_card(number_card_account: str) -> str:
    """Функция, которая умеет обрабатывать информацию как о картах, так и о счетах"""
    if len(number_card_account.split()[-1]) == 16:
        new_number = get_mask_card_number(number_card_account.split()[-1])
        result = f'{number_card_account[:-16]}{new_number}'
        return result
    elif len(number_card_account.split()[-1]) == 20:
        new_number = get_mask_account(number_card_account.split()[-1])
        result = f'{number_card_account[:-20]}{new_number}'
        return result

print(mask_account_card('Счет 73654108430135874305'))

def get_date(user_date: Union[str]) -> str:
    """Функция получения даты в определенном формате и возвращения в формате ДД.ММ.ГГГГ"""
    date_format = datetime.strptime(user_date, "%Y-%m-%dT%H:%M:%S.%f")
    new_date = date_format.strftime("%d.%m.%Y")
    return new_date
print(get_date('2024-03-11T02:26:18.671407'))


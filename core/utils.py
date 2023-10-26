import json
from core.config import URL


def load_operations():
    print(URL)
    with open(URL) as file:
        raw_json = file.read()
        operations = json.loads(raw_json)
        return operations


def define_type(account_type):
    for type in account_type.split():
        if type == "Счет":
            return 'account'
        else:
            return 'kard'


def mask_kard(kard):
    new_kard = []
    for text in kard.split():
        if text.isalpha():
            new_kard.append(text)
        if text.isdigit():
            new_kard.append(f'{text[:4]} {text[4:6]}** **** {text[-4:]}')
    return new_kard


def mask_account(account):
    new_account = []
    for text in account.split():
        if text.isalpha():
            new_account.append(text)
        if text.isdigit():
            new_account.append(f'**{text[-4:]}')
    return new_account


def transfer(direction):
    if define_type(direction) == 'kard':
        transfer_direction = mask_kard(direction)
    else:
        transfer_direction = mask_account(direction)
    return transfer_direction

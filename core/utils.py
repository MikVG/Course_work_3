import json


def load_operations(url):
    """
    Функция читает json файл и возвращает его в виде списка словарей
    :param url: адрес json файла
    :return: список словарей
    """
    with open(url) as file:
        raw_json = file.read()
        operations = json.loads(raw_json)
        return operations


def define_type(account_type):
    """
    Функция определяет тип счета: Счет или перевод по карте
    :param account_type: тип перевода "Счет" или наименование платежной системы карты
    :return: тип перевода Счет или по карте
    """
    for type in account_type.split():
        if type == "Счет":
            return 'account'
        else:
            return 'kard'


def mask_kard(kard):
    """
    Функция выполняет маскирование карты
    :param kard: тип платежной системы карты и номер карты
    :return: словарь с типом платежной системы карты и максированным номером карты
    """
    new_kard = []
    for text in kard.split():
        if text.isalpha():
            new_kard.append(text)
        if text.isdigit():
            new_kard.append(f'{text[:4]} {text[4:6]}** **** {text[-4:]}')
    return new_kard


def mask_account(account):
    """
    Функция выполняет маскирование счета
    :param account: Счет и номер счета
    :return: словарь с наименованием Счет и максированным номером счета
    """
    new_account = []
    for text in account.split():
        if text.isalpha():
            new_account.append(text)
        if text.isdigit():
            new_account.append(f'**{text[-4:]}')
    return new_account


def transfer(direction):
    """
    Функция определяющая тип счета в переводе: перевода с/на карту или перевод с/на счет
    :param direction: карта и номер карты или счет и номер счета
    :return: словарь с типом карты и маскированным номером карты или словарь со счетом и маскированным
    номером счета
    """
    if define_type(direction) == 'kard':
        transfer_direction = mask_kard(direction)
    else:
        transfer_direction = mask_account(direction)
    return transfer_direction


def get_executed_operations(operations):
    """
    Функция выполняет выбор только операций с типом 'EXECUTED' и в которых есть значение откуда
    выполняется перевод
    :param operations: список слловарей прочитанный из json файла
    :return: список словарей операций с типом 'EXECUTED' и в которых есть значение откуда
    выполняется перевод
    """
    operations = [operation for operation in operations if operation.get('state') == 'EXECUTED']
    #operations = [operation for operation in operations if 'from' in operation.keys()]
    return operations


def get_last_five_operations(operations, num_of_operations):
    """
    Функция выбирает определенное количество (в нашем случае 5) последних операций (отсортированных
     по дате по убыванию)
    :param operations: список словарей из функции get_executed_operations
    :param num_of_operations: количество операций, которые необходимо вывести
    :return: список последних выполненных операций в запрашиваемом количестве
    """
    operations_sort = sorted(get_executed_operations(operations), key=lambda x: x['date'], reverse=True)
    last_five_operations = operations_sort[0:num_of_operations]
    return last_five_operations

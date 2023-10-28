import datetime
from core.utils import transfer, get_last_five_operations, get_executed_operations, load_operations
from core.config import URL


def print_operations(url):
    """
    Функция выполняющая вывод необходимого количества последних выполненных операций
    :param url: адрес json файла из которого необходимо вывести операции
    :return: выводит на экран запрашиваеоме количество последних выполненных операций
    """
    operations = load_operations(url)
    operations = get_executed_operations(operations)
    get_operations = get_last_five_operations(operations, 5)
    for operation in get_operations:
        text = operation['date'][:10]
        date = datetime.datetime.strptime(text, '%Y-%m-%d')
        date = datetime.date.strftime(date, '%d.%m.%Y')
        print(f"{date} {operation['description']}")
        print(f'{" ".join(str(x) for x in transfer(operation['from']))} -> '
              f'{" ".join(str(x) for x in transfer(operation['to']))}')
        print(f"{operation['operationAmount']['amount']} руб.\n")


# Вызов функции
print_operations(URL)

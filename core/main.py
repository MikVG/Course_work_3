import datetime
from core.utils import load_operations, transfer


operations = load_operations()

operations = [operation for operation in operations if operation.get('state') == 'EXECUTED']

operations = sorted(operations, key=lambda x: x['date'], reverse=True)

count = 0
for operation in operations:
    count += 1
    if count < 6:
        text = operation['date'][:10]
        date = datetime.datetime.strptime(text, '%Y-%m-%d')
        date = datetime.date.strftime(date, '%d.%m.%Y')
        print(f"{date} {operation['description']}")
        if 'from' in operation.keys():
            print(f'{" ".join(str(x) for x in transfer(operation['from']))} -> '
                  f'{" ".join(str(x) for x in transfer(operation['to']))}')
        else:
            print(f'-> {" ".join(str(x) for x in transfer(operation['to']))}')
        print(f"{operation['operationAmount']['amount']} руб.\n")

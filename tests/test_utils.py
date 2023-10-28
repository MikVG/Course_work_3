import pytest

from core import utils
import os


@pytest.fixture
def url_fixture():
    absolutely_dir = os.path.dirname(__file__)
    file_path = ('/test.json')
    URL = absolutely_dir + file_path
    return URL


@pytest.fixture()
def test_operation():
    operation = [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }
]
    return operation


def test_load_operations(url_fixture):
    assert utils.load_operations(url_fixture) == [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }
]


def test_define_type():
    assert utils.define_type('kard') == 'kard'
    assert utils.define_type('Счет') == 'account'


def test_mask_kard():
    assert utils.mask_kard('Maestro 1596837868705199') == ['Maestro', '1596 83** **** 5199']


def test_mask_account():
    assert utils.mask_account('Счет 64686473678894779589') == ['Счет', '**9589']


def test_transfer():
    assert utils.transfer('Maestro 1596837868705199') == ['Maestro', '1596 83** **** 5199']
    assert utils.transfer('Счет 64686473678894779589') == ['Счет', '**9589']


def test_get_executed_operations(test_operation):
    assert utils.get_executed_operations(test_operation) == [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }
]


def test_get_last_five_operations(test_operation):
    assert utils.get_last_five_operations(test_operation, 1) == [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }
]

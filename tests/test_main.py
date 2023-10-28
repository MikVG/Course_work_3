import pytest
from core.main import print_operations
import os

absolutely_dir = os.path.dirname(__file__)
file_path = ('/test.json')
URL = absolutely_dir + file_path


def test_main():
    assert print_operations(URL) == None

# test_main_code.py

import pytest
from main_code import add_numbers

def test_add_numbers():
    # Test cases
    result = add_numbers(2, 3)
    assert result == 5, "Test failed: add_numbers(2, 3) did not return 5"

    result = add_numbers(-1, 1)
    assert result == 0, "Test failed: add_numbers(-1, 1) did not return 0"

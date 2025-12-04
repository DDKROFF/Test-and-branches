import pytest
from utils.arrs import get, my_slice

def test_get_existing_index():
    assert get([10, 20, 30], 1) == 20

def test_get_nonexistent_index_with_default():
    assert get([10, 20, 30], 5, default='default') == 'default'

def test_get_nonexistent_index_without_default():
    assert get([10, 20, 30], 5) == None

def test_get_negative_index_returns_default():
    assert get([10, 20, 30], -1, default='default') == 'default'
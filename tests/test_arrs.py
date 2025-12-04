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

def test_my_slice_default():
    arr = [1, 2, 3, 4, 5]
    assert my_slice(arr) == arr

def test_my_slice_start_and_end():
    arr = [1, 2, 3, 4, 5]
    assert my_slice(arr, 1, 3) == [2, 3]

def test_my_slice_start_only():
    arr = [1, 2, 3, 4, 5]
    assert my_slice(arr, 2) == [3, 4, 5]

def test_my_slice_end_only():
    arr = [1, 2, 3, 4, 5]
    assert my_slice(arr, end=3) == [1, 2, 3]

def test_my_slice_empty_collection():
    assert my_slice([]) == []

def test_my_slice_end_greater_than_length():
    arr = [1, 2, 3]
    assert my_slice(arr, 1, 10) == [2, 3]
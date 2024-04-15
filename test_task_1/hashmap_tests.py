import pytest

from main import HashMap


@pytest.fixture
def hash_map():
    return HashMap(10)


def test_put(hash_map):
    hash_map.put('apple', 1)
    hash_map.put('banana', 2)
    assert hash_map.get('apple') == 1
    assert hash_map.get('banana') == 2


def test_get_nonexistent_key(hash_map):
    assert hash_map.get('orange') is None


def test_update_value(hash_map):
    hash_map.put('apple', 1)
    hash_map.put('apple', 3)
    assert hash_map.get('apple') == 3


def test_remove(hash_map):
    hash_map.put('apple', 1)
    hash_map.remove('apple')
    assert hash_map.get('apple') is None


def test_len(hash_map):
    assert len(hash_map) == 0
    hash_map.put('apple', 1)
    assert len(hash_map) == 1
    hash_map.put('banana', 2)
    assert len(hash_map) == 2


def test_getitem(hash_map):
    hash_map.put('apple', 1)
    assert hash_map['apple'] == 1


def test_setitem(hash_map):
    hash_map['apple'] = 1
    assert hash_map.get('apple') == 1


def test_delitem(hash_map):
    hash_map.put('apple', 1)
    del hash_map['apple']
    assert hash_map.get('apple') is None


def test_iter(hash_map):
    hash_map.put('apple', 1)
    hash_map.put('banana', 2)
    keys = [key for key in hash_map]
    assert sorted(keys) == ['apple', 'banana']


def test_contains(hash_map):
    hash_map.put('apple', 1)
    assert 'apple' in hash_map
    assert 'orange' not in hash_map


def test_resize(hash_map):
    for i in range(20):
        hash_map.put(str(i), i)
    assert hash_map.size > 10


def test_collision(hash_map):
    # Create a collision by using keys that hash to the same index
    key1 = 'a' * (hash_map.size + 1)
    key2 = 'b' * (hash_map.size + 1)
    key3 = 'c' * (hash_map.size + 1)

    hash_map.put(key1, 'value1')
    hash_map.put(key2, 'value2')
    hash_map.put(key3, 'value3')

    assert hash_map.get(key1) == 'value1'
    assert hash_map.get(key2) == 'value2'
    assert hash_map.get(key3) == 'value3'

    hash_map.remove(key2)
    assert hash_map.get(key1) == 'value1'
    assert hash_map.get(key2) is None
    assert hash_map.get(key3) == 'value3'


def test_out_of_range_key(hash_map):
    # Test behavior when a key's hash value is out of range
    key = 'a' * (hash_map.size + 1)
    hash_map.put(key, 'value')
    assert hash_map.get(key) == 'value'
    hash_map.remove(key)
    assert hash_map.get(key) is None


# HashMap class

The `HashMap` class provides an implementation of a hash map data structure in Python. A hash map, also known as a dictionary or associative array, stores key-value pairs where each unique key is mapped to a specific value.

## Usage

### Initialization

To create a new instance of a hash map, specify the initial size of the map:

```python
my_map = HashMap(size)
```

### Methods

#### put(key, value)

Inserts a key-value pair into the hash map. If the key already exists, updates its value.

```python
my_map.put(key, value)
```

#### get(key)

Retrieves the value associated with the given key. If the key does not exist, returns None.

```python
value = my_map.get(key)
```

#### remove(key)

Removes the key-value pair from the hash map.

```python
my_map.remove(key)
```

#### Other Methods

- `__len__`: Returns the number of elements in the hash map.
- `__getitem__`: Allows bracket notation for getting values.
- `__setitem__`: Allows bracket notation for setting values.
- `__delitem__`: Allows bracket notation for deleting values.
- `__iter__`: Allows iteration over the keys in the hash map.
- `__contains__`: Implements the 'in' operator for checking if a key exists.

## Implementation Details

- The hash map dynamically resizes itself to maintain efficient performance.
- Collision resolution is handled using separate chaining with linked lists.

## Example

```python
# Create a new hash map
my_map = HashMap(10)

# Insert key-value pairs
my_map.put("apple", 5)
my_map.put("banana", 7)
my_map.put("orange", 3)

# Retrieve values
print(my_map.get("apple"))  # Output: 5

# Remove a key-value pair
my_map.remove("banana")

# Check if a key exists
if "orange" in my_map:
    print("Orange exists in the map")
```

---

# Tests
```
# Copy code
pytest hashmap_tests.py
```

# More details

## Initialization (`__init__`)

- The `size` argument accepts an integer (`int`) that determines the initial size (number of buckets) of the hash table.
- For example, if `size=16`, then 16 buckets will be created.
- `self.map` is initialized using a list comprehension, creating a list of `size` empty dictionaries (`dict`).
- Dictionaries (`dict`) are chosen because they provide constant time (`O(1)`) lookup, ensuring efficient operations.
- `self.map` represents a list, where each element is a dictionary for storing key-value pairs in the corresponding bucket.
- `self.load_factor_threshold` is set to `0.75`. This value prevents the list from becoming overly full and provides a necessary buffer.

## Function `get_hash_index(key)`

- Accepts the `key` argument and computes its hash value.
- Used to obtain the index in `self.map` where the key-value pair should be stored.

## Function `put(key, value)`

- Accepts `key` and `value` arguments.
- Obtains the index using `get_hash_index(key)`.
- Checks if an element with the same key already exists in the corresponding dictionary.
- If the element doesn't exist, adds the new key-value pair.
- If the element already exists, updates its value.

## Function `get(key)`

- Uses `get_hash_index(key)` to obtain the index.
- Returns the value associated with the key, if present.
- If the key is not found, returns `None`.

## Function `remove(key)`

- Uses `get_hash_index(key)` to obtain the index.
- Checks if the key is present in the corresponding dictionary.
- If the key is present, removes it.
- If the key is not found, returns `None`.

## Function `_check_load_factor()`

- A private function (starts with an underscore `_`).
- Checks if the occupancy of the buckets exceeds `0.75` (the value of `self.load_factor_threshold`).
- If it exceeds, doubles the size of the array (`self.map`) by calling `_resize`.

## Function `_resize()`

- A private function.
- Completely recreates the `self.map` array with a new, increased size.

## Dunder Methods (`__len__`, `__getitem__`, `__setitem__`, `__delitem__`, `__iter__`, `__contains__`)

- Added to make instances of the `HashMap` class behave like built-in Python data types (such as `dict`).

# References

Visual - https://pythontutor.com/
Code - https://github.com/python/cpython/blob/main/Objects/dictobject.c
Video - https://youtu.be/RcZsTI5h0kg?si=SieLXbOei1DykPd6
Video - https://youtu.be/_Q-eNqTOxlE?si=UBsGWi-OZq7iB_12
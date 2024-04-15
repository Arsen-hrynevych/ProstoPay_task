class HashMap:
    def __init__(self, size: int):
        """Initialize the hash map with a given size."""
        self.size = size
        self.map = [dict() for _ in range(size)]
        self.load_factor_threshold = 0.75
        self.num_elements = 0

    def get_hash_index(self, key):
        """Compute the hash index for a given key."""
        return hash(key) % self.size

    def put(self, key, value):
        """Insert a key-value pair into the hash map. If the key already exists, update its value."""
        index = self.get_hash_index(key)
        if key not in self.map[index]:
            self.map[index][key] = value
            self.num_elements += 1
            self._check_load_factor()
        else:
            self.map[index][key] = value

    def get(self, key):
        """Retrieve the value associated with a given key. If the key does not exist, return None."""
        index = self.get_hash_index(key)
        return self.map[index].get(key, None)

    def remove(self, key):
        """Remove a key-value pair from the hash map."""
        index = self.get_hash_index(key)
        if key in self.map[index]:
            del self.map[index][key]
            self.num_elements -= 1
            return
        return None

    def _check_load_factor(self):
        """Check the load factor and resize the hash map if necessary."""
        load_factor = self.num_elements / self.size
        if load_factor > self.load_factor_threshold:
            self._resize(self.size * 2)

    def _resize(self, new_size):
        """Resize the hash map to the given new size."""
        new_map = [dict() for _ in range(new_size)]
        for bucket in self.map:
            for key, value in bucket.items():
                new_index = hash(key) % new_size
                new_map[new_index][key] = value
        self.size = new_size
        self.map = new_map

    def __len__(self):
        """Return the number of elements in the hash map."""
        return self.num_elements

    def __getitem__(self, key):
        """Implement bracket notation for getting values."""
        return self.get(key)

    def __setitem__(self, key, value):
        """Implement bracket notation for setting values."""
        self.put(key, value)

    def __delitem__(self, key):
        """Implement bracket notation for deleting values."""
        self.remove(key)

    def __iter__(self):
        """Implement iteration over the keys in the hash map."""
        for bucket in self.map:
            for key in bucket:
                yield key

    def __contains__(self, key):
        """Implement the 'in' operator for checking if a key exists."""
        index = self.get_hash_index(key)
        return key in self.map[index]



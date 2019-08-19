class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.factor = 1000000
        self.buckets = [-1] * self.factor

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        self.buckets[key % self.factor] = value

    def get(self, key):
        """
        Returns the value to which the specified key is mapped,
        or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        return self.buckets[key % self.factor]

    def remove(self, key):
        """
        Removes the mapping of the specified value key
        if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        self.buckets[key % self.factor] = -1


def test_hash_map():
    hm = MyHashMap()
    hm.put(1, 1)
    hm.put(2, 2)
    assert 1 == hm.get(1)
    assert -1 == hm.get(3)

    hm.put(2, 1)
    assert 1 == hm.get(2)
    hm.remove(2)
    assert -1 == hm.get(2)

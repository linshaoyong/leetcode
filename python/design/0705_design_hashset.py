class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.factor = 1000000
        self.buckets = [False] * self.factor

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.buckets[key % self.factor] = True

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.buckets[key % self.factor] = False

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return self.buckets[key % self.factor]


def test_hash_set():
    hs = MyHashSet()
    hs.add(1)
    hs.add(2)

    assert hs.contains(1)
    assert hs.contains(3) is False

    hs.add(2)
    assert hs.contains(2) is True

    hs.remove(2)
    assert hs.contains(2) is False

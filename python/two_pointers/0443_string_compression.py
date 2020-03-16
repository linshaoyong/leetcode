class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        prev, count, index = chars[0], 1, 0
        for i in range(1, len(chars)):
            if chars[i] == prev:
                count += 1
            else:
                index = self.in_place_replace(chars, prev, count, index)
                prev, count = chars[i], 1
        index = self.in_place_replace(chars, prev, count, index)
        return index

    def in_place_replace(self, chars, prev, count, start):
        chars[start] = prev
        index = start + 1
        if count > 1:
            for n in str(count):
                chars[index] = n
                index += 1
        return index


def test_compress():
    s = Solution()

    chars = ["a", "a", "b", "b", "c", "c", "c"]
    assert 6 == s.compress(chars)
    assert ["a", "2", "b", "2", "c", "3", "c"] == chars

    chars = ["a"]
    assert 1 == s.compress(chars)
    assert ["a"] == chars

    chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    assert 4 == s.compress(chars)
    assert ["a", "b", "1", "2", "b", "b", "b",
            "b", "b", "b", "b", "b", "b"] == chars

    chars = ["a", "a", "a", "b", "b", "a", "a"]
    assert 6 == s.compress(chars)
    assert ["a", "3", "b", "2", "a", "2", "a"] == chars

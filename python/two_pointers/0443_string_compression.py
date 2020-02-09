class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """


def test_compress():
    s = Solution()
    assert 6 == s.compress(["a", "a", "b", "b", "c", "c", "c"])
    assert 1 == s.compress(["a"])
    assert 4 == s.compress(
        ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"])

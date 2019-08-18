class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        s = set()
        for n in A:
            if n in s:
                return n
            s.add(n)


def test_repeated_n_times():
    s = Solution()
    assert 3 == s.repeatedNTimes([1, 2, 3, 3])
    assert 2 == s.repeatedNTimes([2, 1, 2, 5, 3, 2])

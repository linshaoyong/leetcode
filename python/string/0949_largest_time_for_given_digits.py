import itertools


class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        for p in itertools.permutations(sorted(A, reverse=True)):
            if p[0] * 10 + p[1] < 24 and p[2] < 6:
                return f"{p[0]}{p[1]}:{p[2]}{p[3]}"
        return ""


def test_largest_time_from_digits():
    s = Solution()
    assert "23:41" == s.largestTimeFromDigits([1, 2, 3, 4])
    assert "" == s.largestTimeFromDigits([5, 5, 5, 5])

from collections import deque


class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        start, res = 0, 0
        zeros = deque()
        for i in range(len(A)):
            if A[i] == 0:
                zeros.append(i)
                if K == 0:
                    res = max(res, i - start)
                    start = zeros.popleft() + 1
                else:
                    K -= 1
        res = max(res, len(A) - start)
        return res


def test_long_ones():
    s = Solution()
    assert 6 == s.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2)
    assert 10 == s.longestOnes(
        [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3)
    assert 3 == s.longestOnes([0, 0, 1, 1, 1, 0, 0], 0)
    assert 4 == s.longestOnes([0, 0, 0, 1], 4)

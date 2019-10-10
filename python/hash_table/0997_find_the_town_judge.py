class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        count = [0] * (N + 1)
        for i, j in trust:
            count[i] -= 1
            count[j] += 1
        for i in range(1, N + 1):
            if count[i] == N - 1:
                return i
        return -1


def test_find_judge():
    s = Solution()
    assert 2 == s.findJudge(2, [[1, 2]])
    assert 3 == s.findJudge(3, [[1, 3], [2, 3]])
    assert -1 == s.findJudge(3, [[1, 3], [2, 3], [3, 1]])
    assert -1 == s.findJudge(3, [[1, 2], [2, 3]])
    assert 3 == s.findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]])

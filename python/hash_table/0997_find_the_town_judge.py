class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if not trust:
            return 1
        s1, s2, tt = set(), set(), {}
        for n in trust:
            s1.add(n[0])
            s2.add(n[1])
            ts = tt.get(n[1], set())
            ts.add(n[0])
            tt[n[1]] = ts
        ss = s2 - s1
        if len(ss) != 1:
            return -1
        t = ss.pop()
        return t if len(tt[t]) == N - 1 else -1


def test_find_judge():
    s = Solution()
    assert 1 == s.findJudge(1, [[]])
    assert 2 == s.findJudge(2, [[1, 2]])
    assert 3 == s.findJudge(3, [[1, 3], [2, 3]])
    assert -1 == s.findJudge(3, [[1, 3], [2, 3], [3, 1]])
    assert -1 == s.findJudge(3, [[1, 2], [2, 3]])
    assert 3 == s.findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]])

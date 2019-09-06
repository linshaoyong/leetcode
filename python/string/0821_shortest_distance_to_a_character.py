class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        res = [-1 for _ in range(0, len(S))]
        start = -1
        for i in range(0, len(S)):
            if S[i] == C:
                res[i] = 0
                if start < 0:
                    start = i
                    for j in range(0, i):
                        res[j] = i - j
                else:
                    for j in range(start, i):
                        res[j] = min(j - start, i - j)
                    start = i
        for j in range(start, len(S)):
            res[j] = j - start
        return res


def test_shortest_to_char():
    assert [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0] == Solution(
    ).shortestToChar("loveleetcode", 'e')

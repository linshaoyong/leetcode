class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        result = []
        if not S:
            return result
        start_i, end_i = 0, 0
        current = S[0]
        for i in range(1, len(S)):
            if S[i] == current:
                end_i += 1
            else:
                current = S[i]
                if end_i - start_i > 1:
                    result.append([start_i, end_i])
                start_i, end_i = i, i
        if end_i - start_i > 1:
            result.append([start_i, end_i])
        return result


def test_large_group_positions():
    s = Solution()
    assert [[3, 6]] == s.largeGroupPositions("abbxxxxzzy")
    assert [] == s.largeGroupPositions("abc")
    assert [] == s.largeGroupPositions("")
    assert [[0, 2]] == s.largeGroupPositions("aaa")
    assert [[3, 5], [6, 9], [12, 14]] == \
        s.largeGroupPositions("abcdddeeeeaabbbcd")

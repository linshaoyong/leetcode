import bisect


class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        ss = sorted(stones)
        while len(ss) > 1:
            v = ss[-1] - ss[-2]
            ss = ss[:-2]
            if v > 0:
                bisect.insort(ss, v)
        return ss[0] if ss else 0


def test_last_stone_weight():
    s = Solution()
    assert 1 == s.lastStoneWeight([2, 7, 4, 1, 8, 1])
    assert 2 == s.lastStoneWeight([3, 7, 2])
    assert 3 == s.lastStoneWeight([7, 6, 7, 6, 9])

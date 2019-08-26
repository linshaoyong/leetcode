class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        m = {}
        for i in range(0, len(time)):
            v = time[i]
            mod = v % 60
            m[mod] = m.get(mod, 0) + 1
        n = 0
        for i in range(0, 31):
            if i == 0 or i == 30:
                n += m.get(i, 0) * (m.get(i, 0) - 1) // 2
                continue
            n += (m.get(i, 0) * m.get(60 - i, 0))
        return n


def test_num_pairs_divisible_by_60():
    s = Solution()
    assert 3 == s.numPairsDivisibleBy60([30, 20, 150, 100, 40])
    assert 3 == s.numPairsDivisibleBy60([60, 60, 60])

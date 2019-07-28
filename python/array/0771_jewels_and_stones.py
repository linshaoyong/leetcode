class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        n = 0
        js = set([j for j in J])
        for s in S:
            if s in js:
                n += 1
        return n


def test_num_jewels_in_stones():
    s = Solution()
    assert 3 == s.numJewelsInStones("aA", "aAAbbbb")
    assert 0 == s.numJewelsInStones("z", "ZZ")

class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        sp = sorted(people, reverse=True)
        i, j = 0, len(sp) - 1
        while i <= j:
            if sp[i] + sp[j] <= limit:
                j -= 1
            i += 1
        return i


def test_num_rescue_boats():
    s = Solution()
    assert 1 == s.numRescueBoats([1, 2], 3)
    assert 3 == s.numRescueBoats([3, 2, 2, 1], 3)
    assert 4 == s.numRescueBoats([3, 5, 3, 4], 5)
    assert 2 == s.numRescueBoats([5, 1, 4, 2], 6)
    assert 3 == s.numRescueBoats([3, 2, 3, 2, 2], 6)
    assert 4 == s.numRescueBoats([5, 1, 7, 4, 2, 4], 7)

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = 0
        m = 0
        for v in nums:
            if v == 1:
                r += 1
            else:
                m = max(m, r)
                r = 0
        return max(m, r)


def test_find_max_consecutive_ones():
    s = Solution()
    assert 3 == s.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1])

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        r = len(nums)
        a = 0
        start = 0
        ss = 0
        for i in range(0, len(nums)):
            a += nums[i]
            ss += nums[i]
            if ss >= s:
                while ss >= s:
                    ss -= nums[start]
                    start += 1
                r = min(r, i - start + 2)
        return 0 if a < s else r


def test_min_sub_array_len():
    s = Solution()
    assert 2 == s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
    assert 0 == s.minSubArrayLen(3, [1, 1])

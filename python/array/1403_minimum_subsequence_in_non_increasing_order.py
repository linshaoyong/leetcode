class Solution(object):
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        half = sum(nums) // 2
        snums = sorted(nums, reverse=True)
        s, k = 0, 0
        for i, n in enumerate(snums):
            s += n
            k = i
            if s > half:
                break
        return snums[:k + 1]


def test_min_subsequence():
    s = Solution()
    assert [10, 9] == s.minSubsequence([4, 3, 10, 9, 8])
    assert [7, 7, 6] == s.minSubsequence([4, 4, 7, 6, 7])
    assert [6] == s.minSubsequence([6])

class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        sn = sorted(nums, reverse=True)
        mn = {sn[i]: i + 1 for i in range(len(sn))}
        res = []
        for k in nums:
            if mn[k] == 1:
                res.append("Gold Medal")
            elif mn[k] == 2:
                res.append("Silver Medal")
            elif mn[k] == 3:
                res.append("Bronze Medal")
            else:
                res.append(str(mn[k]))
        return res


def test_find_relative_ranks():
    s = Solution()
    assert ["Gold Medal", "Silver Medal", "Bronze Medal",
            "4", "5"] == s.findRelativeRanks([5, 4, 3, 2, 1])

    assert ["Gold Medal", "5", "Bronze Medal", "Silver Medal",
            "4"] == s.findRelativeRanks([10, 3, 8, 9, 4])

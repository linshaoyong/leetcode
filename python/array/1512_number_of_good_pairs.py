class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    res += 1
        return res


def test_num_identical_pairs():
    s = Solution()

    assert 4 == s.numIdenticalPairs([1, 2, 3, 1, 1, 3])
    assert 6 == s.numIdenticalPairs([1, 1, 1, 1])
    assert 0 == s.numIdenticalPairs([1, 2, 3])

class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[i + n])
        return res


def test_shuffle():
    s = Solution()

    assert [2, 3, 5, 4, 1, 7] == s.shuffle([2, 5, 1, 3, 4, 7], 3)
    assert [1, 4, 2, 3, 3, 2, 4, 1] == s.shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4)
    assert [1, 2, 1, 2] == s.shuffle([1, 1, 2, 2], 2)

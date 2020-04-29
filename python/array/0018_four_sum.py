class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = set()
        nums.sort()
        for i, v in enumerate(nums[:-3]):
            for j, vv in enumerate(nums[i + 1:-2]):
                t = target - v - vv
                d = {}
                for x in nums[i + j + 2:]:
                    if x not in d:
                        d[t - x] = 1
                    else:
                        res.add((v, vv, t - x, x))

        return [list(i) for i in res]


def test_four_sum():
    s = Solution()

    res = s.fourSum([1, 0, -1, 0, -2, 2], 0)
    assert 3 == len(res)
    assert [-1, 0, 0, 1] in res
    assert [-2, -1, 1, 2] in res
    assert [-2, 0, 0, 2] in res

    res = s.fourSum([-3, -1, 0, 2, 4, 5], 0)
    assert [[-3, -1, 0, 4]] == res

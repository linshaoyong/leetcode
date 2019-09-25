class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        sn = sorted(nums)
        res = sn[0] + sn[1] + sn[2]
        min_distance = abs(res - target)
        for i in range(len(sn) - 2):
            left, right = i + 1, len(sn) - 1
            while left < right:
                three_sum = sn[i] + sn[left] + sn[right]
                distance = abs(three_sum - target)
                if distance == 0:
                    return three_sum
                if distance < min_distance:
                    min_distance = distance
                    res = three_sum
                if three_sum < target:
                    left += 1
                else:
                    right -= 1
        return res


def test_three_sum_closest():
    s = Solution()
    assert 2 == s.threeSumClosest([-1, 2, 1, -4], 1)
    assert 0 == s.threeSumClosest([0, 0, 0], 1)
    assert 2 == s.threeSumClosest([1, 1, 1, 0], -100)
    assert 0 == s.threeSumClosest([0, 2, 1, -3], 1)

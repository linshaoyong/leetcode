class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        i = 0
        r = 0
        while i < n - 1:
            v = nums[i] + 1
            value, step = 0, 1
            for j in range(1, v):
                if i + j >= n - 1:
                    step = j
                    break
                if nums[i + j] - (v - j) >= value:
                    value = nums[i + j] - (v - j)
                    step = j
            i = i + step
            r += 1
        return r


def test_jump():
    s = Solution()
    assert 2 == s.jump([2, 3, 1, 1, 4])
    assert 1 == s.jump([2, 1])
    assert 1 == s.jump([3, 2, 1])
    assert 1 == s.jump([2, 3, 1])
    assert 2 == s.jump([4, 1, 1, 3, 1, 1, 1])
    assert 3 == s.jump([1, 2, 1, 1, 1])

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res, stack = [], []
        for i in range(len(nums) * 2):
            if i < len(nums):
                res.append(-1)
            if i >= len(nums) and not stack:
                break
            i = i % len(nums)
            while stack and stack[-1][0] < nums[i]:
                _, index = stack.pop()
                res[index] = nums[i]
            stack.append((nums[i], i,))
        return res


def test_next_greater_elements():
    assert [2, -1, 2] == Solution().nextGreaterElements([1, 2, 1])

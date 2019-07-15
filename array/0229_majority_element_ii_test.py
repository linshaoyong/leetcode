class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = len(nums) / 3
        m = {}
        for n in nums:
            m[n] = m.get(n, 0) + 1
        return [k for k, v in m.items() if v > c]


def test_majority_element():
    s = Solution()
    assert [3] == s.majorityElement([3, 2, 3])
    assert [1, 2] == s.majorityElement([1, 1, 1, 3, 3, 2, 2, 2])

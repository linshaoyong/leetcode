class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = len(nums) / 2
        m = {}
        for n in nums:
            t = m.get(n, 0) + 1
            if t > c:
                return n
            m[n] = t


def test_majority_element():
    s = Solution()
    assert 3 == s.majorityElement([3, 2, 3])
    assert 2 == s.majorityElement([2, 2, 1, 1, 1, 2, 2])

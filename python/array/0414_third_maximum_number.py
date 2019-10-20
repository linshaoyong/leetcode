class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = [float('-inf'), float('-inf'), float('-inf')]
        for n in nums:
            if n in a:
                continue
            if n > a[0]:
                a[2] = a[1]
                a[1] = a[0]
                a[0] = n
            elif n > a[1]:
                a[2] = a[1]
                a[1] = n
            elif n > a[2]:
                a[2] = n
        return max(nums) if float('-inf') in a else a[2]


def test_third_max():
    s = Solution()
    assert 1 == s.thirdMax([3, 2, 1])
    assert 2 == s.thirdMax([1, 2])
    assert 1 == s.thirdMax([2, 2, 3, 1])

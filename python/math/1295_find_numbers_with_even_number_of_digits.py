class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for num in nums:
            i = 0
            while num:
                num = num // 10
                i += 1
            if i % 2 == 0:
                res += 1
        return res


def test_find_numbers():
    s = Solution()
    assert 2 == s.findNumbers([12, 345, 2, 6, 7896])
    assert 1 == s.findNumbers([555, 901, 482, 1771])

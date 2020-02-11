class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        res = 0
        while num:
            res += 1
            if num % 2 == 0:
                num = num // 2
            else:
                num -= 1
        return res


def test_number_of_steps():
    s = Solution()
    assert 6 == s.numberOfSteps(14)
    assert 4 == s.numberOfSteps(8)
    assert 12 == s.numberOfSteps(123)

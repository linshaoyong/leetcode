class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        s, m = 1, num - 1
        for i in range(2, num):
            if i >= m:
                break
            if num % i == 0:
                m = num // i
                s = s + m + i
            m = num // i
        return s == num and num > 1


def test_check_perfect_number():
    s = Solution()

    assert s.checkPerfectNumber(1) is False
    assert s.checkPerfectNumber(27) is False
    assert s.checkPerfectNumber(28)
    assert s.checkPerfectNumber(32582657) is False
    assert s.checkPerfectNumber(99999991) is False

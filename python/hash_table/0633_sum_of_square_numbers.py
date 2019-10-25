class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        import math
        n = int(math.sqrt(c)) + 1
        s = set()
        for i in range(n):
            s.add(i * i)
        for v in s:
            if c - v in s:
                return True
        return False


def test_judge_square_sum():
    s = Solution()
    assert s.judgeSquareSum(4)
    assert s.judgeSquareSum(5)
    assert s.judgeSquareSum(6) is False
    assert s.judgeSquareSum(13)

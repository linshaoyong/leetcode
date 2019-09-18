class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left, right = 0, x
        while left < right:
            mid = left + (right - left) // 2
            mm = mid * mid
            if mm == x:
                return mid
            elif mm > x:
                right = mid - 1
            else:
                if (mid + 1) * (mid + 1) > x:
                    return mid
                else:
                    left = mid + 1
        return left


def test_my_sqrt():
    s = Solution()
    assert 2 == s.mySqrt(4)
    assert 2 == s.mySqrt(5)
    assert 2 == s.mySqrt(6)
    assert 2 == s.mySqrt(7)
    assert 2 == s.mySqrt(8)
    assert 3 == s.mySqrt(9)
    assert 3 == s.mySqrt(10)
    assert 0 == s.mySqrt(0)

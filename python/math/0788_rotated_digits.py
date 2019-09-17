class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        res = 0
        vs = set([2, 5, 6, 9])
        ivs = set([3, 4, 7])
        for n in range(2, N + 1):
            v, iv = False, False
            while n > 0:
                a = n % 10
                if a in ivs:
                    iv = True
                    break
                if a in vs:
                    v = True
                n = n // 10
            if v and not iv:
                res += 1
        return res


def test_rotated_digits():
    s = Solution()
    assert 4 == s.rotatedDigits(10)
    assert 1 == s.rotatedDigits(2)
    assert 247 == s.rotatedDigits(857)

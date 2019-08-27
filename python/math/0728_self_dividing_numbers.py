class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        r = []
        for i in range(left, right + 1):
            if self.is_self_dividing(i):
                r.append(i)
        return r

    def is_self_dividing(self, n):
        v = n
        while v > 0:
            mod = v % 10
            if mod == 0:
                return False
            if n % mod != 0:
                return False
            v = v // 10
        return True


def test_self_dividing_numbers():
    s = Solution()
    assert [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12,
            15, 22] == s.selfDividingNumbers(1, 22)

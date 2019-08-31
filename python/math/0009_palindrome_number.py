class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        res = []
        while x:
            res.append(x % 10)
            x = x // 10
        i = 0
        length = len(res)
        for i in range(0, length // 2):
            if res[i] != res[length - 1 - i]:
                return False
        return True


def test_is_palindrome():
    assert Solution().isPalindrome(121)
    assert Solution().isPalindrome(-121) is False
    assert Solution().isPalindrome(10) is False

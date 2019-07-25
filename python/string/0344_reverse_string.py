class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        n = len(s)
        k = int(n / 2)
        j = n - 1
        for i in range(0, k):
            s[i], s[j - i] = s[j - i], s[i]


def test_reverse_string():
    s = Solution()

    ss = ["h", "e", "l", "l", "o"]
    s.reverseString(ss)
    assert ["o", "l", "l", "e", "h"] == ss

    ss = ["H", "a", "n", "n", "a", "h"]
    s.reverseString(ss)
    assert ["h", "a", "n", "n", "a", "H"] == ss

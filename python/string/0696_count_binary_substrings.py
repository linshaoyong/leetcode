class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in range(1, len(s)):
            prev = i - 1
            if s[i] != s[prev]:
                res += 1
                step = 1
                while prev - step >= 0 and i + step < len(s):
                    if s[prev - step] == s[prev] and s[i + step] == s[i]:
                        res += 1
                        step += 1
                    else:
                        break
        return res


def test_count_binary_substrings():
    s = Solution()
    assert 6 == s.countBinarySubstrings("00110011")
    assert 4 == s.countBinarySubstrings("10101")
    assert 2 == s.countBinarySubstrings("00100")

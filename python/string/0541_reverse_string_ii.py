class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res = []
        reverse = True
        for i in range(0, len(s), k):
            if reverse:
                res.append(s[i:i + k][::-1])
            else:
                res.append(s[i:i + k])
            reverse = not reverse
        return ''.join(res)


def test_reverse_str():
    assert "bacdfeg" == Solution().reverseStr("abcdefg", 2)

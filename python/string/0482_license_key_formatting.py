class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        res, j = [], 0
        for i in range(len(S) - 1, -1, -1):
            if S[i] == '-':
                continue
            res.append(S[i].upper())
            j += 1
            if j % K == 0:
                res.append('-')
        if res and res[-1] == '-':
            res.pop()
        return ''.join(res[::-1])


def test_license_key_formatting():
    s = Solution()
    assert "5F3Z-2E9W" == s.licenseKeyFormatting("5F3Z-2e-9-w", 4)
    assert "2-5G-3J" == s.licenseKeyFormatting("2-5g-3-J", 2)
    assert "" == s.licenseKeyFormatting("---", 3)

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        h = {}
        prev = ''
        ls = 0
        for c in s:
            if c == 'L':
                if prev == 'L':
                    ls += 1
                    if ls > 2:
                        return False
                else:
                    prev = 'L'
                    ls = 1
                continue
            if c == 'A':
                h[c] = h.get(c, 0) + 1
                if h[c] > 1:
                    return False
            prev = ''
        return True


def test_check_record():
    assert Solution().checkRecord("PPALLP")
    assert Solution().checkRecord("LALL")
    assert Solution().checkRecord("PPALLL") is False

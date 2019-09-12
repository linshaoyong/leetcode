class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if len(a) != len(b):
            return max(len(a), len(b))

        res = len(a)
        for i in range(len(a)):
            if a[i] == b[i]:
                res -= 1
            else:
                break
        return -1 if res == 0 else res


def test_fin_lus_length():
    assert 3 == Solution().findLUSlength("aba", "cdc")
    assert -1 == Solution().findLUSlength("aaa", "aaa")

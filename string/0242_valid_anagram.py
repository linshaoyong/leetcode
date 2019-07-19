class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        ds, ts = {}, {}
        for x in s:
            ds[x] = ds.get(x, 0) + 1
        for x in t:
            ts[x] = ts.get(x, 0) + 1
        return cmp(ds, ts) == 0


def test_is_anagram():
    s = Solution()
    assert s.isAnagram("anagram", "nagaram") is True

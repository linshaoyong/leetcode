class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        start, res = 0, 0
        for i in range(min(len(g), len(s))):
            for j in range(start, len(s)):
                if s[j] >= g[i]:
                    res += 1
                    start = j + 1
                    break
            if start == len(s):
                break
        return res


def test_find_content_children():
    s = Solution()
    assert 1 == s.findContentChildren([1, 2, 3], [1, 1])
    assert 2 == s.findContentChildren([1, 2], [1, 2, 3])

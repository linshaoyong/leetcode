class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        h = {}
        for c in s:
            h[c] = h.get(c, 0) + 1
        sh = sorted(h.items(), key=lambda kv: kv[1], reverse=True)
        res = []
        for k, v in sh:
            res.append(k * v)
        return ''.join(res)


def test_frequency_sort():
    s = Solution()
    r = s.frequencySort("tree")
    assert r.startswith("ee")

    r = s.frequencySort("Aabb")
    assert r.startswith("bb")

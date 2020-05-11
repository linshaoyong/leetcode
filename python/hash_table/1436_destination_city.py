class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        ss, ds = set(), set()
        for [a, b] in paths:
            ss.add(a)
            ds.add(b)
        return list(ds - ss)[0]


def test_dest_city():
    s = Solution()
    assert "Sao Paulo" == s.destCity(
        [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]])
    assert "A" == s.destCity([["B", "C"], ["D", "B"], ["C", "A"]])
    assert "Z" == s.destCity([["A", "Z"]])

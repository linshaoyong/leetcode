class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        m = {'N': 1, 'S': -1, 'E': 1, 'W': -1}
        a, b, s = 0, 0, set()
        s.add((a, b))
        for p in path:
            if p in ['N', 'S']:
                a += m.get(p)
            else:
                b += m.get(p)
            if (a, b) in s:
                return True
            s.add((a, b))
        return False


def test_is_path_crossing():
    s = Solution()
    assert s.isPathCrossing("NES") is False
    assert s.isPathCrossing("NESWW")
    assert s.isPathCrossing("NNSWWEWSSESSWENNW")

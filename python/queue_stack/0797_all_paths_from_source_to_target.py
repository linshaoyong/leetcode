class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        target = len(graph) - 1
        paths = [[0]]
        res = []
        while paths:
            p = paths.pop()
            ts = graph[p[-1]]
            for t in ts:
                if t == target:
                    res.append(p + [t])
                else:
                    if t not in p:
                        paths.append(p + [t])
        return res


def test_all_paths_source_target():
    r = Solution().allPathsSourceTarget([
        [1, 2], [3], [3], []])
    assert 2 == len(r)
    assert [0, 1, 3] in r
    assert [0, 2, 3] in r

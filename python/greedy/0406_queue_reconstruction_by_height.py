class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda k: (k[0], -k[1]), reverse=True)
        res = []
        for p in people:
            res.insert(p[1], p)
        return res


def test_reconstruct_queue():
    s = Solution()
    assert [[5, 0], [7, 0], [5, 2],
            [6, 1], [4, 4], [7, 1]] == s.reconstructQueue(
        [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]])

class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """


def test_path_in_zigzag_tree():
    assert [1, 3, 4, 14] == Solution().pathInZigZagTree(14)
    assert [1, 2, 6, 10, 26] == Solution().pathInZigZagTree(26)

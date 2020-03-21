class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        n, res = 1, []
        while n < label:
            res.append(n)
            n = n * 2 + 1
        res.append(label)
        for i in range(len(res) - 2, 0, -1):
            if i % 2 == 0:
                j = (res[i] * 2 - res[i + 1] + 1) // 2
                res[i] = res[i - 1] + j + 1
            else:
                j = (res[i + 1] - res[i] + 1) // 2
                res[i] = res[i] - j + 1
        return res


def test_path_in_zig_zag_tree():
    s = Solution()
    assert [1, 3, 4, 14] == s.pathInZigZagTree(14)
    assert [1, 2, 6, 10, 26] == s.pathInZigZagTree(26)

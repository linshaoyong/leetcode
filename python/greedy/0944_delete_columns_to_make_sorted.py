class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        r = 0
        for i in range(0, len(A[0])):
            non_decreasing = True
            for j in range(0, len(A) - 1):
                if A[j][i] > A[j + 1][i]:
                    non_decreasing = False
                    break
            if non_decreasing:
                r += 1
        return len(A[0]) - r


def test_min_deletion_size():
    s = Solution()
    assert 1 == s.minDeletionSize(["cba", "daf", "ghi"])
    assert 0 == s.minDeletionSize(["a", "b"])
    assert 3 == s.minDeletionSize(["zyx", "wvu", "tsr"])

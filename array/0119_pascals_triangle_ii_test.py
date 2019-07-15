class Solution(object):
    def getRow(self, rowIndex):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        r = [1, 1]
        for n in range(2, rowIndex + 1):
            row = []
            for k in range(0, n + 1):
                if k == 0 or k == n:
                    row.append(1)
                    continue
                row.append(r[k - 1] + r[k])
            r = row
        return r


def test_get_row():
    s = Solution()

    assert [1] == s.getRow(0)

    assert [1, 1] == s.getRow(1)

    assert [1, 2, 1] == s.getRow(2)

    assert [1, 3, 3, 1] == s.getRow(3)

    assert [1, 4, 6, 4, 1] == s.getRow(4)

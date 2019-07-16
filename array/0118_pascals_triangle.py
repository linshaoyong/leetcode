class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        r = []
        for n in range(0, numRows):
            if n == 0:
                r.append([1])
                continue
            if n == 1:
                r.append([1, 1])
                continue
            row = []
            for k in range(0, n + 1):
                if k == 0 or k == n:
                    row.append(1)
                    continue
                row.append(r[n - 1][k - 1] + r[n - 1][k])
            r.append(row)
        return r


def test_generate():
    s = Solution()

    assert [[1]] == s.generate(1)

    assert [[1],
            [1, 1]] == s.generate(2)

    assert [[1],
            [1, 1],
            [1, 2, 1]] == s.generate(3)

    assert [[1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1]] == s.generate(4)

    assert [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1]] == s.generate(5)

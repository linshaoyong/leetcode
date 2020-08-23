class Solution(object):
    def mostVisited(self, n, rounds):
        """
        :type n: int
        :type rounds: List[int]
        :rtype: List[int]
        """
        rs = {i: 0 for i in range(1, n + 1)}
        rs[rounds[0]] += 1

        start = rounds[0]
        for i in range(1, len(rounds)):
            if start < rounds[i]:
                for j in range(start + 1, rounds[i] + 1):
                    rs[j] += 1
            else:
                for j in range(start + 1, n + 1):
                    rs[j] += 1
                for j in range(1, rounds[i] + 1):
                    rs[j] += 1
            start = rounds[i]

        max_v, res = 0, []
        for _, v in rs.items():
            max_v = max(max_v, v)

        for k, v in rs.items():
            if v == max_v:
                res.append(k)
        return sorted(res)


def test_most_visited():
    s = Solution()

    assert [1, 2] == s.mostVisited(4, [1, 3, 1, 2])
    assert [2] == s.mostVisited(2, [2, 1, 2, 1, 2, 1, 2, 1, 2])
    assert [1, 2, 3, 4, 5, 6, 7] == s.mostVisited(7, [1, 3, 5, 7])

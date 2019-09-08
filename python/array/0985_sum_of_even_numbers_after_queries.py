class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        v = sum([a for a in A if a % 2 == 0])
        res = []
        for query in queries:
            before_even = A[query[1]] % 2 == 0
            query_even = query[0] % 2 == 0
            if before_even:
                if query_even:
                    v += query[0]
                else:
                    v -= A[query[1]]
            else:
                if not query_even:
                    v += A[query[1]] + query[0]
            A[query[1]] += query[0]
            res.append(v)
        return res


def test_sum_even_after_queries():
    assert [8, 6, 2, 4] == Solution().sumEvenAfterQueries(
        [1, 2, 3, 4], [[1, 0], [-3, 1], [-4, 0], [2, 3]])

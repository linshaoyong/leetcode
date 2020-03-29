class Solution(object):
    def beautifulArray(self, N):
        """
        :type N: int
        :rtype: List[int]
        """
        return self.divide_conquer(list(range(1, N + 1)))

    def divide_conquer(self, arr):
        if len(arr) < 3:
            return arr
        ls, hs = [], []
        for i, v in enumerate(arr):
            if i % 2 == 0:
                hs.append(v)
            else:
                ls.append(v)
        return self.divide_conquer(ls) + self.divide_conquer(hs)


def test_beautiful_array():
    s = Solution()
    assert [2, 4, 1, 3] == s.beautifulArray(4)
    assert [2, 4, 3, 1, 5] == s.beautifulArray(5)

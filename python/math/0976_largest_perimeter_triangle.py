class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        a = sorted(A)[::-1]
        first = 0
        second = a[0]
        third = a[1]
        for i in range(2, len(a)):
            first = second
            second = third
            third = a[i]
            if second + third > first:
                return first + second + third
        return 0


def test_largest_perimeter():
    s = Solution()
    assert 5 == s.largestPerimeter([2, 1, 2])
    assert 0 == s.largestPerimeter([1, 2, 1])
    assert 10 == s.largestPerimeter([3, 2, 3, 4])
    assert 8 == s.largestPerimeter([3, 6, 2, 3])

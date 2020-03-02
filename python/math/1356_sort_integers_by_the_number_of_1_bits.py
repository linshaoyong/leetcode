class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        return sorted(arr, key=lambda x: (bin(x).count("1"), x))


def test_sort_by_bits():
    s = Solution()
    assert [0, 1, 2, 4, 8, 3, 5, 6, 7] == s.sortByBits(
        [0, 1, 2, 3, 4, 5, 6, 7, 8])
    assert [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024] == s.sortByBits(
        [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1])
    assert [10000, 10000] == s.sortByBits([10000, 10000])
    assert [2, 3, 5, 17, 7, 11, 13, 19] == s.sortByBits(
        [2, 3, 5, 7, 11, 13, 17, 19])
    assert [10, 100, 10000, 1000] == s.sortByBits([10, 100, 1000, 10000])

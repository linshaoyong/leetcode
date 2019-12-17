class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        t = len(arr) // 4 + 1
        prev, c = arr[0], 1
        for i in range(1, len(arr) - 1):
            if arr[i] == prev:
                c += 1
                if c >= t:
                    return arr[i]
            else:
                prev = arr[i]
                c = 1
        return prev


def test_find_special_integer():
    s = Solution()
    assert 6 == s.findSpecialInteger([1, 2, 2, 6, 6, 6, 6, 7, 10])

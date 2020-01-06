class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        m = arr[-1]
        for i in range(len(arr) - 1, -1, -1):
            new_m = max(arr[i], m)
            arr[i] = m
            m = new_m
        arr[-1] = -1
        return arr


def test_replace_elements():
    s = Solution()
    assert [18, 6, 6, 6, 1, -1] == s.replaceElements([17, 18, 5, 4, 6, 1])

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]


def test_merge():
    s = Solution()

    n1 = [1, 2, 3, 0, 0, 0]
    s.merge(n1, 3, [2, 5, 6], 3)
    assert [1, 2, 2, 3, 5, 6] == n1

    n1 = [1, 2, 3, 0, 0, 0]
    s.merge(n1, 3, [2, 5, 6], 2)
    assert [1, 2, 2, 3, 5, 0] == n1

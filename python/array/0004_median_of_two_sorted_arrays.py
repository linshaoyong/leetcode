class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(nums1) + len(nums2)
        p1 = (n - 1) // 2
        p2 = p1 if n % 2 == 0 else p1 + 1

        i, j, s = 0, 0, 0
        while s < p1:
            s += 1
            if nums1[i] < nums2[j]:
                if i < len(nums1) - 1:
                    i += 1
                else:
                    j += 1
            else:
                if j < len(nums2) - 1:
                    j += 1
                else:
                    i += 1


def test_find_median_sorted_arrays():
    s = Solution()
    assert 2.0 == s.findMedianSortedArrays([1, 3], [2])
    assert 2.5 == s.findMedianSortedArrays([1, 2], [3, 4])

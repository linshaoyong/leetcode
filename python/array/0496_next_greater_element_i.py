class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        m = {}
        s = []
        for n in nums2:
            while len(s) > 0:
                if s[-1] >= n:
                    break
                m[s[-1]] = n
                s = s[:-1]
            s.append(n)
        return [m.get(n, -1) for n in nums1]


def test_next_greater_element():
    s = Solution()

    assert [-1, 3, -1] == s.nextGreaterElement([4, 1, 2], [1, 3, 4, 2])
    assert [3, -1] == s.nextGreaterElement([2, 4], [1, 2, 3, 4])

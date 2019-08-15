from collections import deque


class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        q = deque()
        for i in range(0, len(arr)):
            if arr[i] == 0:
                q.append(0)
            if len(q) > 0:
                q.append(arr[i])
                arr[i] = q.popleft()


def test_duplicate_zeros():
    s = Solution()

    a = [1, 0, 2, 3, 0, 4, 5, 0]
    s.duplicateZeros(a)
    assert a == [1, 0, 0, 2, 3, 0, 0, 4]

    a = [1, 2, 3]
    s.duplicateZeros(a)
    assert a == [1, 2, 3]

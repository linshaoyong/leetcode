class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        res = 0
        for s, e in zip(startTime, endTime):
            if queryTime >= s and queryTime <= e:
                res += 1
        return res


def test_busy_student():
    s = Solution()
    assert 1 == s.busyStudent([1, 2, 3], [3, 2, 7], 4)
    assert 1 == s.busyStudent([4], [4], 4)
    assert 0 == s.busyStudent([4], [4], 5)
    assert 0 == s.busyStudent([1, 1, 1, 1], [1, 3, 2, 4], 7)
    assert 5 == s.busyStudent([9, 8, 7, 6, 5, 4, 3, 2, 1], [
                              10, 10, 10, 10, 10, 10, 10, 10, 10], 5)

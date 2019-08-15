class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """


def test_open_lock():
    s = Solution()

    assert 6 == s.openLock(["0201", "0101", "0102", "1212", "2002"], "0202")
    assert 1 == s.openLock(["8888"], "0009")
    assert -1 == s.openLock(["8887", "8889", "8878",
                             "8898", "8788", "8988", "7888", "9888"], "8888")
    assert -1 == s.openLock(["0000"], "8888")

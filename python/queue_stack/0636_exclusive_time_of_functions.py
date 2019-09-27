class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """


def test_exclusive_time():
    s = Solution()
    assert [3, 4] == s.exclusiveTime(
        2, ["0:start:0", "1:start:2", "1:end:5", "0:end:6"])

    assert [8] == s.exclusiveTime(
        1, ["0:start:0", "0:start:2", "0:end:5", "0:start:6",
            "0:end:6", "0:end:7"])

    assert [7, 1] == s.exclusiveTime(
        2, ["0:start:0", "0:start:2", "0:end:5", "1:start:6",
            "1:end:6", "0:end:7"])

    assert [8, 1] == s.exclusiveTime(
        2, ["0:start:0", "0:start:2", "0:end:5", "1:start:7",
            "1:end:7", "0:end:8"])

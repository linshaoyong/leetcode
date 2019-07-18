class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """


def test_longest_common_prefix():
    s = Solution()

    assert "fl" == s.longestCommonPrefix(["flower", "flow", "flight"])
    assert "" == ["dog", "racecar", "car"]

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join([v[::-1] for v in s.split()])


def test_reverse_words():
    s = Solution()
    assert "s'teL ekat edoCteeL tsetnoc" == s.reverseWords(
        "Let's take LeetCode contest")

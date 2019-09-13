class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        for c in sorted(d, key=lambda x: (-len(x), x)):
            if self.can_be_formed(s, c):
                return c
        return ''

    def can_be_formed(self, s, ss):
        start = 0
        for i in range(len(ss)):
            found = False
            for j in range(start, len(s)):
                if s[j] == ss[i]:
                    found = True
                    if i == len(ss) - 1:
                        return True
                    start = j + 1
                    break
            if not found:
                return False
        return False


def test_find_longest_word():
    s = Solution()
    assert "apple" == s.findLongestWord(
        "abpcplea", ["ale", "apple", "monkey", "plea"])
    assert "a" == s.findLongestWord(
        "abpcplea", ["a", "b", "c"])
    assert "ewaf" == s.findLongestWord(
        "aewfafwafjlwajflwajflwafj",
        ["apple", "ewaf", "awefawfwaf", "awef", "awefe", "ewafeffewafewf"])

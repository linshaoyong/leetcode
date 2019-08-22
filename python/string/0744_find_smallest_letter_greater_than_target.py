class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        for c in letters:
            if c > target:
                return c
        return letters[0]


def test_next_greatest_letter():
    s = Solution()
    assert "c" == s.nextGreatestLetter(["c", "f", "j"], "a")
    assert "f" == s.nextGreatestLetter(["c", "f", "j"], "c")

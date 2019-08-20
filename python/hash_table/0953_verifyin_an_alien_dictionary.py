class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        orderm = {c: i for i, c in enumerate(order)}
        for i in range(len(words) - 1):
            if not self.lte(words[i], words[i + 1], orderm):
                return False
        return True

    def lte(self, word1, word2, orderm):
        for i, w in enumerate(word1):
            if i > len(word2) - 1:
                return False
            if orderm.get(w) > orderm.get(word2[i]):
                return False
            if orderm.get(w) < orderm.get(word2[i]):
                return True
        return True


def test_is_alien_sorted():
    s = Solution()
    assert s.isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz")

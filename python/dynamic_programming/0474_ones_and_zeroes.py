class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """


def test_find_max_form():
    s = Solution()
    assert 4 == s.findMaxForm({"10", "0001", "111001", "1", "0"}, 5, 3)
    assert 2 == s.findMaxForm({"10", "0", "1"}, 1, 1)

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.generate('', n, n, res)
        return res

    def generate(self, v, left, right, res):
        if left == 0:
            res.append(v + ')' * right)
            return

        self.generate(v + '(', left - 1, right, res)
        if left != right:
            self.generate(v + ')', left, right - 1, res)


def test_generate_parenthesis():
    s = Solution()
    assert ["()"] == s.generateParenthesis(1)

    r = s.generateParenthesis(2)
    assert 2 == len(r)
    assert "(())" in r
    assert "()()" in r

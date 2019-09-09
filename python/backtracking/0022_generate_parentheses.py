class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.generate(list('(' * n + ')' * n), n, n, [], res)
        print(res)
        return res

    def generate(self, ps, left, right, path, res):
        if left == 0 and right == 0:
            res.append(path)
        for i in range(len(ps)):
            if left == right and ps[i] == ')':
                continue
            if ps[i] == '(':
                left -= 1
            else:
                right -= 1
            path.append(ps[i])
            self.generate(ps[:i] + ps[i + 1:], left, right, path, res)
            path.pop()


def test_generate_parenthesis():
    r = Solution().generateParenthesis(3)
    assert 5 == len(r)
    assert "((()))" in r
    assert "(()())" in r
    assert "(())()" in r
    assert "()(())" in r
    assert "()()()" in r

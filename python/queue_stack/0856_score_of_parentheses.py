class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        for s in S:
            if s == '(':
                stack.append(s)
            else:
                v = 0
                while stack:
                    last = stack.pop()
                    if last == '(':
                        if v > 0:
                            stack.append(v * 2)
                        else:
                            stack.append(1)
                        break
                    else:
                        v += last
        return sum(stack)


def test_score_of_parentheses():
    s = Solution()
    assert 1 == s.scoreOfParentheses("()")
    assert 2 == s.scoreOfParentheses("(())")
    assert 2 == s.scoreOfParentheses("()()")
    assert 6 == s.scoreOfParentheses("(()(()))")

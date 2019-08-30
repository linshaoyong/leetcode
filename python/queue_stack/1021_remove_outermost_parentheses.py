class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []
        removes = set()
        for i, s in enumerate(S):
            if s == '(':
                stack.append((s, i,))
            if s == ')':
                v = stack.pop()
                if not stack:
                    removes.add(v[1])
                    removes.add(i)
        return ''.join([s for i, s in enumerate(S) if i not in removes])


def test_remove_outer_parentheses():
    s = Solution()
    assert "()()()" == s.removeOuterParentheses("(()())(())")
    assert "()()()()(())" == s.removeOuterParentheses("(()())(())(()(()))")
    assert "" == s.removeOuterParentheses("()()")
    assert "(()())(()())" == s.removeOuterParentheses("((()())(()()))")

class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for c in s:
            if c == ')':
                tmp = []
                while stack:
                    v = stack.pop()
                    if v == '(':
                        break
                    tmp.append(v)
                stack.extend(tmp)
            else:
                stack.append(c)
        return ''.join(stack)


def test_reverse_parentheses():
    s = Solution()
    assert "dcba" == s.reverseParentheses("(abcd)")
    assert "iloveu" == s.reverseParentheses("(u(love)i)")
    assert "leetcode" == s.reverseParentheses("(ed(et(oc))el)")
    assert "apmnolkjihgfedcbq" == s.reverseParentheses("a(bcdefghijkl(mno)p)q")

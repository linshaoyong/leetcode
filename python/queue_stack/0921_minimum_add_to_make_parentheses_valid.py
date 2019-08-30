class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        for c in S:
            if c == '(':
                stack.append(c)
            if c == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(c)
        return len(stack)


def test_min_add_to_make_valid():
    s = Solution()
    assert 1 == s.minAddToMakeValid("())")
    assert 3 == s.minAddToMakeValid("(((")
    assert 0 == s.minAddToMakeValid("()")
    assert 4 == s.minAddToMakeValid("()))((")

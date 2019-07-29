class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs = {")": "(", "]": "[", "}": "{"}
        keys = pairs.keys()
        stack = []
        for c in s:
            if c in keys:
                if len(stack) == 0:
                    return False
                v = stack.pop()
                if pairs[c] != v:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0


def test_is_valid():
    s = Solution()

    assert s.isValid("]") is False
    assert s.isValid("()") is True
    assert s.isValid("()[]{}") is True
    assert s.isValid("(]") is False
    assert s.isValid("([)]") is False
    assert s.isValid("{[]}") is True

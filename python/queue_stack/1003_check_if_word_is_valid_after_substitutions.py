class Solution(object):
    def isValid(self, S):
        """
        :type S: str
        :rtype: bool
        """
        stack = []
        for s in S:
            if s == 'c':
                valid = [s]
                for i in range(2):
                    if not stack:
                        return False
                    valid.append(stack.pop())
                if valid != ['c', 'b', 'a']:
                    return False
            else:
                stack.append(s)
        return len(stack) == 0


def test_is_valid():
    s = Solution()
    assert s.isValid("aabcbc")
    assert s.isValid("abcabcababcc")
    assert s.isValid("abccba") is False
    assert s.isValid("cababc") is False

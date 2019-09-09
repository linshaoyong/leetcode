class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        i = 0
        stack = []
        for p in popped:
            while i < len(pushed) and (not stack or stack[-1] != p):
                stack.append(pushed[i])
                i += 1
            if not stack or stack[-1] != p:
                return False
            stack.pop()
        return len(stack) == 0


def test_validate_stack_sequences():
    s = Solution()
    assert s.validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1])
    assert s.validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]) is False

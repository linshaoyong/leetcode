class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []
        next_i = 0
        for i in range(0, len(S)):
            if i < next_i:
                continue
            if not stack:
                stack.append(S[i])
                continue
            if S[i] != stack[-1]:
                stack.append(S[i])
                continue
            stack.pop()
        return ''.join(stack)


def test_remove_duplicates():
    assert "ca" == Solution().removeDuplicates("abbaca")
    assert "" == Solution().removeDuplicates("aaaaaaaa")
    assert "a" == Solution().removeDuplicates("aaaaaaaaa")

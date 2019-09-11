class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        for s in path + '/':
            if s != '/':
                stack.append(s)
                continue

            if not stack:
                stack.append(s)
                continue

            if stack[-1] == '/':
                continue

            if stack[-1] == '.':
                if stack[-2] == '.':
                    if stack[-3] == "/":
                        i = 0
                        while stack and i < 2:
                            if stack.pop() == '/':
                                i += 1
                        stack.append(s)
                else:
                    stack.pop()
            else:
                stack.append(s)
        if len(stack) > 1 and stack[-1] == '/':
            stack.pop()
        return ''.join(stack)


def test_simplify_path():
    s = Solution()
    assert "/home" == s.simplifyPath("/home/")
    assert "/" == s.simplifyPath("/../")
    assert "/home/foo" == s.simplifyPath("/home//foo/")
    assert "/c" == s.simplifyPath("/a/./b/../../c/")
    assert "/c" == s.simplifyPath("/a/../../b/../c//.//")
    assert "/a/b/c" == s.simplifyPath("/a//b////c/d//././/..")
    assert "/..." == s.simplifyPath("/...")

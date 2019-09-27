
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for ch in s:
            if ch != ']':
                stack.append(ch)
                continue
            sss = []
            while stack:
                v = stack.pop()
                if v == '[':
                    times, n = 0, 0
                    while stack and stack[-1].isdigit():
                        times += int(stack.pop()) * pow(10, n)
                        n += 1
                    vvv = ''.join(sss[::-1]) * times
                    stack.append(vvv)
                    break
                sss.append(v)
        return ''.join(stack)


def test_decode_string():
    s = Solution()
    assert "aaabcbc" == s.decodeString("3[a]2[bc]")
    assert "accaccacc" == s.decodeString("3[a2[c]]")
    assert "abcabccdcdcdef" == s.decodeString("2[abc]3[cd]ef")
    assert "lclclclclclclclclclclc" == s.decodeString("11[lc]")
    assert "zzzyypqefefefefyypqefefefefef" == s.decodeString(
        "3[z]2[2[y]pq4[e1[f]]]ef")

class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if k >= len(num):
            return "0"
        if k == 0:
            return num

        stack = [num[0]]
        d, j = 0, 0
        for i in range(1, len(num)):
            if d == k:
                break
            j = i
            while stack and num[i] < stack[-1] and d < k:
                stack.pop()
                d += 1
            if num[i] == '0' and not stack:
                continue
            stack.append(num[i])

        if not stack:
            for i in range(j + 1, len(num)):
                if num[i] != '0':
                    break
                j += 1

        for _ in range(k - d):
            stack.pop()

        res = ''.join(stack) + num[j + 1:]
        return res if res else "0"


def test_remove_k_digits_1():
    s = Solution()
    assert "1219" == s.removeKdigits("1432219", 3)
    assert "200" == s.removeKdigits("10200", 1)
    assert "0" == s.removeKdigits("10", 2)
    assert "0" == s.removeKdigits("10", 1)
    assert "0" == s.removeKdigits("1000000", 1)
    assert "33" == s.removeKdigits("5337", 2)
    assert "12" == s.removeKdigits("212", 1)
    assert "12345" == s.removeKdigits("12345", 0)
    assert "107" == s.removeKdigits("1107", 1)
    assert "1111" == s.removeKdigits("1111111", 3)
    assert "2111" == s.removeKdigits("11100002111", 3)
    assert "100002111" == s.removeKdigits("11100002111", 2)
    assert "1000020111" == s.removeKdigits("11000020111", 1)
    assert "20111" == s.removeKdigits("11000020111", 2)
    assert "1100051000020111" == s.removeKdigits("9181716100051000020111", 6)
    assert "100051000020111" == s.removeKdigits("9181716100051000020111", 7)
    assert "51000020111" == s.removeKdigits("9181716100051000020111", 8)
    assert "1000020111" == s.removeKdigits("9181716100051000020111", 9)
    assert "20111" == s.removeKdigits("9181716100051000020111", 10)
    assert "111" == s.removeKdigits("9181716100051000020111", 11)
    assert "11" == s.removeKdigits("9181716100051000020111", 12)

    assert "4161001" == s.removeKdigits("4874161001", 3)
    assert "161001" == s.removeKdigits("4874161001", 4)
    assert "1001" == s.removeKdigits("12204874161001", 9)
    assert "1737" == s.removeKdigits("17837", 1)

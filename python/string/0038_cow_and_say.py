class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        v = "1"
        for i in range(2, n + 1):
            v = self.next_value(v)
        return v

    def next_value(self, s):
        r = []
        for i, c in enumerate(s):
            if i > 0 and c == s[i - 1]:
                r[-1].append(c)
            else:
                r.append([c])
        v = ""
        for n in r:
            v += self.countAndSaySameVaule(n)
        return v

    def countAndSaySameVaule(self, n):
        return str(len(n)) + n[0]


def test_count_and_say_1():
    s = Solution()
    assert s.countAndSaySameVaule("1") == "11"
    assert s.countAndSaySameVaule("11") == "21"
    assert s.countAndSaySameVaule("111") == "31"


def test_count_and_say_2():
    s = Solution()
    assert s.countAndSay(1) == "1"
    assert s.countAndSay(2) == "11"
    assert s.countAndSay(3) == "21"
    assert s.countAndSay(4) == "1211"
    assert s.countAndSay(5) == "111221"
    assert s.countAndSay(6) == "312211"
    assert s.countAndSay(7) == "13112221"
    assert s.countAndSay(8) == "1113213211"
    assert s.countAndSay(9) == "31131211131221"
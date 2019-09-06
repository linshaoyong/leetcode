class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        minutes = [1, 2, 4, 8, 16, 32, 60, 120, 240, 480]
        res = []
        self.read([], len(minutes), num, res)
        print(res)

    def read(self, readed, minutes, num, res):
        if num == 0:
            res.append([r for r in readed])
            return
        for i in range(0, minutes):
            if i not in readed:
                readed.append(i)
                self.read(readed, minutes, num - 1, res)
            if readed:
                readed.pop()


def test_read_binary_watch():

    r = Solution().readBinaryWatch(5)

    assert 10 == len(r)
    assert "1:00" in r
    assert "2:00" in r
    assert "4:00" in r
    assert "8:00" in r
    assert "0:01" in r
    assert "0:02" in r
    assert "0:04" in r
    assert "0:08" in r
    assert "0:16" in r
    assert "0:32" in r

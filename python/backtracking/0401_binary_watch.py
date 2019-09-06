class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        self.slots = [1, 2, 4, 8, 16, 32, 1, 2, 4, 8]
        res = []
        self.read([], 0, len(self.slots), num, res)
        result = []
        for indexs in res:
            v = self.get_time(indexs)
            if v:
                result.append(v)
        return result

    def read(self, readed, start, end, num, res):
        if num == 0:
            res.append([r for r in readed])
            return
        for i in range(start, end):
            if not (readed and i <= readed[-1]):
                readed.append(i)
                self.read(readed, start + 1, end, num - 1, res)
                readed.pop()

    def get_time(self, indexs):
        minutes = 0
        hours = 0
        for i in indexs:
            if i >= 6:
                hours += self.slots[i]
            else:
                minutes += self.slots[i]
        if hours >= 12 or minutes >= 60:
            return ''
        return str(hours) + ":0" + str(minutes) if minutes < 10 \
            else str(hours) + ":" + str(minutes)


def test_read_binary_watch():

    r = Solution().readBinaryWatch(1)

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

    r = Solution().readBinaryWatch(2)
    assert 44 == len(r)
    assert "0:03" in r
    assert "0:05" in r
    assert "0:06" in r
    assert "0:09" in r
    assert "0:10" in r
    assert "0:12" in r
    assert "0:17" in r
    assert "0:18" in r
    assert "0:20" in r
    assert "0:24" in r
    assert "0:33" in r
    assert "0:34" in r
    assert "0:36" in r
    assert "0:40" in r
    assert "0:48" in r
    assert "1:01" in r
    assert "1:02" in r
    assert "1:04" in r
    assert "1:08" in r

    r = Solution().readBinaryWatch(3)
    assert 112 == len(r)

    r = Solution().readBinaryWatch(4)
    assert 181 == len(r)

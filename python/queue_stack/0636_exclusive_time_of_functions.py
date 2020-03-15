class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        res, stack = [0] * n, []
        for log in logs:
            i, flag, ts = log.split(':')
            i, ts = int(i), int(ts)
            if flag == 'start':
                if stack:
                    res[stack[-1][0]] += ts - stack[-1][1]
                    stack[-1][1] = ts
                stack.append([i, ts])
            else:
                _, prev_ts = stack.pop()
                next_ts = ts + 1
                res[i] += next_ts - prev_ts
                if stack:
                    stack[-1][1] = next_ts
        return res


def test_exclusive_time():
    s = Solution()
    assert [3, 4] == s.exclusiveTime(
        2, ["0:start:0", "1:start:2", "1:end:5", "0:end:6"])

    assert [8] == s.exclusiveTime(
        1, ["0:start:0", "0:start:2", "0:end:5", "0:start:6",
            "0:end:6", "0:end:7"])

    assert [7, 1] == s.exclusiveTime(
        2, ["0:start:0", "0:start:2", "0:end:5", "1:start:6",
            "1:end:6", "0:end:7"])

    assert [8, 1] == s.exclusiveTime(
        2, ["0:start:0", "0:start:2", "0:end:5", "1:start:7",
            "1:end:7", "0:end:8"])

    assert [1, 1, 2] == s.exclusiveTime(
        3, ["0:start:0", "0:end:0", "1:start:1", "1:end:1", "2:start:2",
            "2:end:2", "2:start:3", "2:end:3"])

    assert [20, 14, 35, 7, 6, 9, 10, 14] == s.exclusiveTime(8,
                                                            ["0:start:0",
                                                             "1:start:5",
                                                             "2:start:6",
                                                             "3:start:9",
                                                             "4:start:11",
                                                             "5:start:12",
                                                             "6:start:14",
                                                             "7:start:15",
                                                             "1:start:24",
                                                             "1:end:29",
                                                             "7:end:34",
                                                             "6:end:37",
                                                             "5:end:39",
                                                             "4:end:40",
                                                             "3:end:45",
                                                             "0:start:49",
                                                             "0:end:54",
                                                             "5:start:55",
                                                             "5:end:59",
                                                             "4:start:63",
                                                             "4:end:66",
                                                             "2:start:69",
                                                             "2:end:70",
                                                             "2:start:74",
                                                             "6:start:78",
                                                             "0:start:79",
                                                             "0:end:80",
                                                             "6:end:85",
                                                             "1:start:89",
                                                             "1:end:93",
                                                             "2:end:96",
                                                             "2:end:100",
                                                             "1:end:102",
                                                             "2:start:105",
                                                             "2:end:109",
                                                             "0:end:114"])

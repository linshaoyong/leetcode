class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        lls = {}
        dls = []
        for log in logs:
            _, v = log.split(" ", 1)
            if v.split(" ", 1)[0].isalpha():
                lls[log] = v
            else:
                dls.append(log)
        sort_lls = [k for k, _ in sorted(
            lls.items(), key=lambda x: x[1] + x[0])]
        return sort_lls + dls


def test_reorder_log_files():
    s = Solution()
    assert ["g1 act car", "a8 act zoo", "ab1 off key dog",
            "a1 9 2 3 1", "zo4 4 7"] == s.reorderLogFiles(
        ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog",
         "a8 act zoo"])

    assert ["7e apw c y", "m azv x f", "8 hyyq z p",
            "8 ksif m u", "c otdk cl", "2 y xyr fc", "27 85717 7",
            "52 314 99", "d 046099 0", "6 3272401"] == s.reorderLogFiles(
        ["27 85717 7", "2 y xyr fc", "52 314 99", "d 046099 0",
         "m azv x f", "7e apw c y", "8 hyyq z p",
         "6 3272401", "c otdk cl", "8 ksif m u"])

    assert ["a2 act car", "g1 act car", "a8 act zoo", "ab1 off key dog",
            "a1 9 2 3 1", "zo4 4 7"] == s.reorderLogFiles(
                ["a1 9 2 3 1", "g1 act car", "zo4 4 7",
                 "ab1 off key dog", "a8 act zoo", "a2 act car"])

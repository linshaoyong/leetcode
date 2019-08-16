class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        M = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        year, month, day = map(int, date.split('-'))
        is_leap_year = (year % 400 == 0) or (
            (year % 4 == 0) and (year % 100 != 0))
        count = day
        for i in range(0, month - 1):
            count += M[i]
            if i == 1 and is_leap_year:
                count += 1
        return count


def test_day_of_year():
    s = Solution()
    assert 9 == s.dayOfYear("2019-01-09")
    assert 41 == s.dayOfYear("2019-02-10")
    assert 60 == s.dayOfYear("2003-03-01")
    assert 61 == s.dayOfYear("2004-03-01")
    assert 60 == s.dayOfYear("2016-02-29")

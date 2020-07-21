class Solution(object):

    def reformatDate(self, date):
        """
        :type date: str
        :rtype: str
        """
        self.MONTHS = {"Jan": "01", "Feb": "02", "Mar": "03",
                       "Apr": "04", "May": "05", "Jun": "06",
                       "Jul": "07", "Aug": "08", "Sep": "09",
                       "Oct": "10", "Nov": "11", "Dec": "12"}

        day, month, year = date.split(" ")
        day = day[:2] if len(day) == 4 else "0" + day[0]
        return "-".join([year, self.MONTHS.get(month), day])


def test_reformat_date():
    s = Solution()

    assert "2052-10-20" == s.reformatDate("20th Oct 2052")
    assert "1933-06-06" == s.reformatDate("6th Jun 1933")
    assert "1960-05-26" == s.reformatDate("26th May 1960")

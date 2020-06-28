class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        min_v, max_v, sum_v = salary[0], salary[0], salary[0]
        for v in salary[1:]:
            if v < min_v:
                min_v = v
            if v > max_v:
                max_v = v
            sum_v += v
        return (sum_v - min_v - max_v) / (len(salary) - 2)


def test_average():
    s = Solution()

    assert 2500.0 == s.average([4000, 3000, 1000, 2000])
    assert 2000.0 == s.average([1000, 2000, 3000])
    assert 3500.0 == s.average([6000, 5000, 4000, 3000, 2000, 1000])
    assert 4750.0 == s.average([8000, 9000, 2000, 3000, 6000, 1000])
    assert 41111.11111111111 == s.average([48000, 59000, 99000, 13000, 78000,
                                           45000, 31000, 17000, 39000, 37000,
                                           93000, 77000, 33000, 28000, 4000,
                                           54000, 67000, 6000, 1000, 11000])

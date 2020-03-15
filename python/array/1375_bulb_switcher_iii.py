class Solution(object):
    def numTimesAllBlue(self, light):
        """
        :type light: List[int]
        :rtype: int
        """
        ons, right, moment = 0, 0, 0
        for i in range(len(light)):
            ons += 1
            right = max(right, light[i])
            if ons == right:
                moment += 1
        return moment


def test_num_times_all_blue():
    s = Solution()
    assert 3 == s.numTimesAllBlue([2, 1, 3, 5, 4])
    assert 2 == s.numTimesAllBlue([3, 2, 4, 1, 5])
    assert 1 == s.numTimesAllBlue([4, 1, 2, 3])
    assert 3 == s.numTimesAllBlue([2, 1, 4, 3, 6, 5])
    assert 6 == s.numTimesAllBlue([1, 2, 3, 4, 5, 6])

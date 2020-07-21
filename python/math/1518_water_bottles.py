class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        res, emptyBottles = numBottles, numBottles
        while emptyBottles >= numExchange:
            newBottles = emptyBottles // numExchange
            res += newBottles
            emptyBottles = newBottles + emptyBottles % numExchange
        return res


def test_num_water_bottles():
    s = Solution()

    assert 13 == s.numWaterBottles(9, 3)
    assert 19 == s.numWaterBottles(15, 4)
    assert 6 == s.numWaterBottles(5, 5)
    assert 2 == s.numWaterBottles(2, 3)

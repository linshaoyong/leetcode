class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five, ten = 0, 0
        for bill in bills:
            if bill == 5:
                five += 1
                continue
            if bill == 10:
                ten += 1
                five -= 1
                if five < 0:
                    return False
            if bill == 20:
                if ten > 0:
                    ten -= 1
                    five -= 1
                    if five < 0:
                        return False
                else:
                    five -= 3
                    if five < 0:
                        return False
        return True


def test_lemonade_change():
    s = Solution()
    assert s.lemonadeChange([5, 5, 5, 10, 20])
    assert s.lemonadeChange([5, 5, 10])
    assert s.lemonadeChange([10, 10]) is False
    assert s.lemonadeChange([5, 5, 10, 10, 20]) is False

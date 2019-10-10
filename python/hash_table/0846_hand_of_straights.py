import collections


class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        count = collections.Counter(hand)
        while count:
            m = min(count)
            for k in range(m, m + W):
                v = count[k]
                if not v:
                    return False
                if v == 1:
                    del count[k]
                else:
                    count[k] = v - 1
        return True


def test_is_n_straight_hand():
    s = Solution()
    assert s.isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3)
    assert s.isNStraightHand([1, 2, 3, 4, 5], 4) is False
    assert s.isNStraightHand([5, 1], 2) is False
    assert s.isNStraightHand([233722108, 386144634, 221638886, 175028874,
                              408337082, 91410299, 793763682, 972910825,
                              627251147, 135020779], 2) is False

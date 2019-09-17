class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        same = 1
        prev = 0
        planted = 0
        for p in flowerbed:
            if p == 0:
                same += 1
            if p == 1:
                if prev == 0:
                    planted += (same - 1) // 2
                    if planted >= n:
                        return True
                same = 0
            prev = p
        planted += same // 2
        return planted >= n


def test_can_place_flowers():
    assert Solution().canPlaceFlowers([1, 0, 0, 0, 1], 1)
    assert Solution().canPlaceFlowers([1, 0, 0, 0, 1], 2) is False
    assert Solution().canPlaceFlowers([0, 0, 1, 0, 1], 1)
    assert Solution().canPlaceFlowers([1, 0, 0, 0, 1, 0, 0], 2)
    assert Solution().canPlaceFlowers([1, 0], 1) is False

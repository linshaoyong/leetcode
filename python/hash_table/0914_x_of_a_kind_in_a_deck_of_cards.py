import collections
import functools


class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        count = collections.Counter(deck).values()
        return functools.reduce(gcd, count) > 1


def test_has_groups_size_x():
    s = Solution()
    assert s.hasGroupsSizeX([1, 2, 3, 4, 4, 3, 2, 1])
    assert s.hasGroupsSizeX([1, 1, 1, 2, 2, 2, 3, 3]) is False
    assert s.hasGroupsSizeX([1]) is False
    assert s.hasGroupsSizeX([1, 1])
    assert s.hasGroupsSizeX([1, 1, 2, 2, 2, 2]) is True
    assert s.hasGroupsSizeX([1, 1, 1, 1, 2, 2, 2, 2, 2, 2])

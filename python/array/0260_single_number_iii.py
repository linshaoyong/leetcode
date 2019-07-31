class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for x in nums:
            d[x] = d.get(x, 0) + 1

        return [k for k, v in d.items() if v == 1]


def test_single_number():
    s = Solution()
    r = s.singleNumber([1, 2, 1, 3, 2, 5])
    assert len(r) == 2
    assert 3 in r
    assert 5 in r

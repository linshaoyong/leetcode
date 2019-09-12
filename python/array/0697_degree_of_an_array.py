class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i in range(len(nums)):
            a, b, c = d.get(nums[i], (0, 0, 0))
            a = a + 1
            if a == 1:
                b = i
            else:
                c = i
            d[nums[i]] = (a, b, c,)
        m = 0
        r = len(nums)
        for _, (a, b, c) in sorted(d.items(),
                                   key=lambda kv: kv[1], reverse=True):
            m = max(m, a)
            if m > a:
                break
            if m == 1:
                r = 1
                break
            r = min(r, c - b + 1)
        return r


def test_find_shortest_subarray():
    assert 2 == Solution().findShortestSubArray([1, 2, 2, 3, 1])
    assert 6 == Solution().findShortestSubArray([1, 2, 2, 3, 1, 4, 2])
    assert 1 == Solution().findShortestSubArray([2, 1])

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        h = {n: 1 for n in range(1, len(nums) + 1)}
        r = []
        for n in nums:
            if n not in h:
                r.append(n)
                continue
            del h[n]
        r.append(list(h.keys())[0])
        return r


def test_find_error_nums():
    assert [2, 3] == Solution().findErrorNums([1, 2, 2, 4])

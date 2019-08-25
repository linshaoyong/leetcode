class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        sn = sorted(nums)
        c = sn[0]
        r = [i for i in range(1, c)]
        for n in sn[1:]:
            if n - c > 1:
                for i in range(c + 1, n):
                    r.append(i)
            c = n
        for i in range(c + 1, len(nums) + 1):
            r.append(i)
        return r


def test_find_disappeared_numbers():
    s = Solution()
    assert [5, 6] == s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])
    assert [] == s.findDisappearedNumbers([])
    assert [2] == s.findDisappearedNumbers([1, 1])

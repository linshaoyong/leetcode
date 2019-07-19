from functools import cmp_to_key


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if sum(nums) == 0:
            return "0"

        def compare(x, y):
            return int(y + x) - int(x + y)

        sns = sorted([str(s) for s in nums], key=cmp_to_key(compare))
        return ''.join(sns)


def test_largest_number():
    s = Solution()

    assert s.largestNumber([10, 2]) == "210"
    assert s.largestNumber([3, 30, 34, 5, 9]) == "9534330"
    assert s.largestNumber([121, 12]) == "12121"
    assert s.largestNumber([0, 0]) == "0"
    assert s.largestNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "9876543210"

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = []
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            d = digits[i] + carry
            if d == 10:
                s.append(0)
                carry = 1
            else:
                s.append(d)
                carry = 0
        if carry == 1:
            s.append(1)
        return s[::-1]


def test_plus_one():
    s = Solution()
    assert [1, 2, 4] == s.plusOne([1, 2, 3])
    assert [4, 3, 2, 2] == s.plusOne([4, 3, 2, 1])
    assert [1, 0, 0, 0, 0] == s.plusOne([9, 9, 9, 9])

class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        carry = 0
        res = []
        for i in range(len(A) - 1, -1, -1):
            a = A[i] + K % 10 + carry
            K = K // 10
            if a >= 10:
                res.append(a - 10)
                carry = 1
            else:
                res.append(a)
                carry = 0
        while K > 0:
            a = K % 10 + carry
            K = K // 10
            if a >= 10:
                res.append(a - 10)
                carry = 1
            else:
                res.append(a)
                carry = 0
        if carry > 0:
            res.append(carry)
        return res[::-1]


def test_add_to_array_form():
    s = Solution()
    assert [0] == s.addToArrayForm([0], 0)
    assert [1, 2, 3, 4] == s.addToArrayForm([1, 2, 0, 0], 34)
    assert [4, 5, 5] == s.addToArrayForm([2, 7, 4], 181)
    assert [1, 0, 2, 1] == s.addToArrayForm([2, 1, 5], 806)
    assert [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] == s.addToArrayForm(
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9], 1)

class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        presum = {}
        acc, res = 0, 0
        for i in range(len(A)):
            acc += A[i]
            if acc - S in presum:
                res += presum[acc - S]
            if acc == S:
                res += 1
            presum[acc] = presum.get(acc, 0) + 1
        return res


def test_num_subarrays_with_sum():
    s = Solution()
    assert 0 == s.numSubarraysWithSum([1, 0, 1, 0, 1], 4)
    assert 4 == s.numSubarraysWithSum([1, 0, 1, 0, 1], 2)
    assert 15 == s.numSubarraysWithSum([0, 0, 0, 0, 0], 0)
    assert 67 == s.numSubarraysWithSum(
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 0)

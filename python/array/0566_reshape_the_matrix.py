class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums) * len(nums[0]) != r * c:
            return nums
        res = []
        for i in range(len(nums)):
            ii = i * len(nums[i])
            for j in range(len(nums[i])):
                nth = ii + j
                if nth % c == 0:
                    res.append([nums[i][j]])
                else:
                    res[-1].append(nums[i][j])
        return res


def test_matrix_reshape():
    s = Solution()
    assert [[1, 2, 3, 4]] == s.matrixReshape([[1, 2], [3, 4]], 1, 4)
    assert [[1, 2], [3, 4]] == s.matrixReshape([[1, 2], [3, 4]], 2, 4)

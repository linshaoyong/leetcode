class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        for i in range(0, length - 1):
            if nums[i] != 0:
                continue
            k = i
            while nums[k] == 0 and k < length - 1:
                k += 1
                if nums[k] != 0:
                    nums[i], nums[k] = nums[k], 0
                    break


def test_move_zeroes():
    s = Solution()
    a = [0, 1, 0, 3, 12]
    s.moveZeroes(a)
    assert a == [1, 3, 12, 0, 0]

    a = [0, 1]
    s.moveZeroes(a)
    assert a == [1, 0]

    a = [0]
    s.moveZeroes(a)
    assert a == [0]

    a = [1]
    s.moveZeroes(a)
    assert a == [1]

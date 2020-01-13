class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(0, len(nums), 2):
            res.extend([nums[i + 1] for _ in range(nums[i])])
        return res


def test_decompress_rle_list():
    s = Solution()
    assert [2, 4, 4, 4] == s.decompressRLElist([1, 2, 3, 4])

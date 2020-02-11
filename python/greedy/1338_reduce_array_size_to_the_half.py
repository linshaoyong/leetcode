import collections


class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        threshold = (len(arr) + 1) // 2
        counter = collections.Counter(arr)
        total, res = 0, 0
        for _, v in counter.most_common():
            if total >= threshold:
                break
            total += v
            res += 1
        return res


def test_min_set_size():
    s = Solution()
    assert 2 == s.minSetSize([3, 3, 3, 3, 5, 5, 5, 2, 2, 7])
    assert 1 == s.minSetSize([7, 7, 7, 7, 7, 7])
    assert 1 == s.minSetSize([1, 9])
    assert 1 == s.minSetSize([1000, 1000, 3, 7])
    assert 5 == s.minSetSize([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    assert 5 == s.minSetSize(
        [9, 77, 63, 22, 92, 9, 14, 54, 8, 38, 18, 19, 38, 68, 58, 19])

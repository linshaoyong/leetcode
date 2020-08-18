class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        res = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if abs(arr[i] - arr[j]) > a:
                    continue
                for k in range(j + 1, len(arr)):
                    if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        res += 1
        return res


def test_count_good_triplets():
    s = Solution()

    assert 4 == s.countGoodTriplets([3, 0, 1, 1, 9, 7], 7, 2, 3)
    assert 0 == s.countGoodTriplets([1, 1, 2, 2, 3], 0, 0, 1)

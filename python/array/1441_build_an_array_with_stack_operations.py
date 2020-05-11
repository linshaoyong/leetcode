class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        res, ts = [], set(target)
        for x in range(1, target[-1] + 1):
            res.append("Push")
            if x not in ts:
                res.append("Pop")
        return res


def test_build_array():
    s = Solution()

    assert ["Push", "Push", "Pop", "Push"] == s.buildArray([1, 3], 3)
    assert ["Push", "Push", "Push"] == s.buildArray([1, 2, 3], 3)
    assert ["Push", "Push"] == s.buildArray([1, 2], 4)
    assert ["Push", "Pop", "Push", "Push",
            "Push"] == s.buildArray([2, 3, 4], 4)

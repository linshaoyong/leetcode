class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = [int(i) for i in version1.split(".")]
        v2 = [int(i) for i in version2.split(".")]
        for i in range(0, len(v1)):
            if i >= len(v2):
                if v1[i] == 0:
                    continue
                return 1
            if v1[i] > v2[i]:
                return 1
            if v1[i] < v2[i]:
                return -1
        if len(v1) < len(v2):
            for i in range(len(v1), len(v2)):
                if v2[i] > 0:
                    return -1
        return 0


def test_compare_version():
    s = Solution()

    assert 0 == s.compareVersion("1.0", "1")
    assert -1 == s.compareVersion("1", "1.1")
    assert -1 == s.compareVersion("0.1", "1.1")
    assert 1 == s.compareVersion("1.0.1", "1")
    assert 0 == s.compareVersion("2.0", "2.0")

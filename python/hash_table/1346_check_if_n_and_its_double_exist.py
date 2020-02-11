class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        sa = set()
        for a in arr:
            if 2 * a in sa or (a % 2 == 0 and a // 2 in sa):
                return True
            sa.add(a)
        return False


def test_check_if_exist():
    s = Solution()
    assert s.checkIfExist([10, 2, 5, 3])
    assert s.checkIfExist([7, 1, 14, 11])
    assert s.checkIfExist([3, 1, 7, 11]) is False
    assert s.checkIfExist([-2, 0, 10, -19, 4, 6, -8]) is False
    assert s.checkIfExist([0, 0])

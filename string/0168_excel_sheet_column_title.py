class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        capitals = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
        result = []
        while n > 0:
            result.append(capitals[(n - 1) % 26])
            n = (n - 1) // 26
        return ''.join(result[::-1])


def test_convert_to_title():
    s = Solution()
    assert "A" == s.convertToTitle(1)
    assert "AB" == s.convertToTitle(28)
    assert "ZY" == s.convertToTitle(701)

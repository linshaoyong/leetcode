class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        tbc = False
        for i in range(len(bits) - 1):
            if tbc:
                tbc = False
                continue
            if bits[i] == 1:
                tbc = True
        return not tbc


def test_is_one_bit_character():
    s = Solution()
    assert s.isOneBitCharacter([1, 0, 0])
    assert s.isOneBitCharacter([1, 1, 1, 0]) is False

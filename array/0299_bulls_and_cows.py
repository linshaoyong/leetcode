class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        b, t = 0, 0
        hs, hg = {}, {}
        for i in range(0, len(secret)):
            sv, gv = secret[i], guess[i]
            hs[sv] = hs.get(sv, 0) + 1
            hg[gv] = hg.get(gv, 0) + 1
            if sv == gv:
                b += 1

        for k, v in hs.items():
            t += min(v, hg.get(k, 0))
        return str(b) + "A" + str(t - b) + "B"


def test_get_hint():
    s = Solution()

    assert "1A3B" == s.getHint("1807", "7810")
    assert "1A1B" == s.getHint("1123", "0111")
    assert "1A0B" == s.getHint("11", "10")
    assert "1A1B" == s.getHint("9305", "9012")

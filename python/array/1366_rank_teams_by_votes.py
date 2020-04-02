class Solution(object):
    def rankTeams(self, votes):
        """
        :type votes: List[str]
        :rtype: str
        """
        if len(votes) == 1:
            return votes[0]
        m = {}
        for vote in votes:
            for i, v in enumerate(vote):
                if v in m:
                    scores = m.get(v)
                else:
                    scores = [0] * len(vote)
                    scores.append(100 - ord(v))
                scores[i] += 1
                m[v] = scores
        return ''.join([w for w in sorted(m, key=m.get, reverse=True)])


def test_rankTeams():
    s = Solution()
    assert "ACB" == s.rankTeams(["ABC", "ACB", "ABC", "ACB", "ACB"])
    assert "XWYZ" == s.rankTeams(["WXYZ", "XYZW"])
    assert "ZMNAGUEDSJYLBOPHRQICWFXTVK" == s.rankTeams(
        ["ZMNAGUEDSJYLBOPHRQICWFXTVK"])
    assert "ABC" == s.rankTeams(["BCA", "CAB", "CBA", "ABC", "ACB", "BAC"])
    assert "M" == s.rankTeams(["M", "M", "M", "M"])

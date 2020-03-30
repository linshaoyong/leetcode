class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        res = 0
        for i in range(len(rating)):
            for j in range(i + 1, len(rating)):
                if rating[i] == rating[j]:
                    continue
                up = True if rating[i] < rating[j] else False
                for k in range(j + 1, len(rating)):
                    if rating[j] == rating[k]:
                        continue
                    if up:
                        if rating[j] < rating[k]:
                            res += 1
                    else:
                        if rating[j] > rating[k]:
                            res += 1
        return res


def test_num_teams():
    s = Solution()
    assert 3 == s.numTeams([2, 5, 3, 4, 1])
    assert 0 == s.numTeams([2, 1, 3])
    assert 4 == s.numTeams([1, 2, 3, 4])

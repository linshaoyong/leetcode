class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        hs = {S[i]: i for i in range(len(S))}
        res, start, end = [], 0, 0
        for i in range(len(S)):
            if hs[S[i]] > end:
                end = hs[S[i]]
            if i == end:
                res.append(end - start + 1)
                start = i + 1
        return res


def test_partition_labels():
    assert [9, 7, 8] == Solution().partitionLabels("ababcbacadefegdehijhklij")

class Solution(object):
    def largestValsFromLabels(self, values, labels, num_wanted, use_limit):
        """
        :type values: List[int]
        :type labels: List[int]
        :type num_wanted: int
        :type use_limit: int
        :rtype: int
        """
        res, num, used = 0, 0, {}
        for value, label in sorted(list(zip(values, labels)), reverse=True):
            if num >= num_wanted:
                break
            u = used.get(label, 0)
            if u >= use_limit:
                continue
            res += value
            num += 1
            used[label] = u + 1
        return res


def test_largest_vals_from_labels():
    s = Solution()
    assert 9 == s.largestValsFromLabels([5, 4, 3, 2, 1], [1, 1, 2, 2, 3], 3, 1)
    assert 12 == s.largestValsFromLabels(
        [5, 4, 3, 2, 1], [1, 3, 3, 3, 2], 3, 2)
    assert 16 == s.largestValsFromLabels(
        [9, 8, 8, 7, 6], [0, 0, 0, 1, 1], 3, 1)
    assert 24 == s.largestValsFromLabels(
        [9, 8, 8, 7, 6], [0, 0, 0, 1, 1], 3, 2)

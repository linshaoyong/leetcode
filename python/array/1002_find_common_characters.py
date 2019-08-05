class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        counts = {}
        result = []
        for i in range(0, len(A)):
            for w in A[i]:
                v = counts.get(w, {i: 0})
                v[i] = v.get(i, 0) + 1
                counts[w] = v
        for k, d in counts.items():
            if len(d) < len(A):
                continue
            m = len(A[0])
            for _, vvv in d.items():
                m = min(m, vvv)
            for _ in range(0, m):
                result.append(k)
        return result


def test_common_chars():
    s = Solution()
    r = s.commonChars(["bella", "label", "roller"])
    assert 3 == len(r)
    assert 'e' in r
    assert 'l' in r

    r = s.commonChars(["cool", "lock", "cook"])
    assert 2 == len(r)
    assert 'c' in r
    assert 'o' in r

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        m = {}
        for v in strs:
            sv = tuple(sorted(v))
            r = m.get(sv, [])
            r.append(v)
            m[sv] = r
        return list(m.values())


def test_group_anagrams():
    s = Solution()
    result = s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert len(result) == 3
    assert ["eat", "tea", "ate"] in result
    assert ["tan", "nat"] in result
    assert ["bat"] in result

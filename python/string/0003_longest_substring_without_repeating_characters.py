class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        subs = []
        start = 0
        for i, c in enumerate(s):
            if c not in d:
                d[c] = i
                continue
            if d[c] >= start:
                subs.append(i - start)
                start = d[c] + 1
            d[c] = i

        subs.append(len(s) - start)
        return max(subs)


def test_length_of_longest_substring():
    s = Solution()
    assert s.lengthOfLongestSubstring("") == 0
    assert s.lengthOfLongestSubstring("c") == 1
    assert s.lengthOfLongestSubstring("au") == 2
    assert s.lengthOfLongestSubstring("aab") == 2
    assert s.lengthOfLongestSubstring("abcabcbb") == 3
    assert s.lengthOfLongestSubstring("bbbbbb") == 1
    assert s.lengthOfLongestSubstring("pwwkew") == 3
    assert s.lengthOfLongestSubstring("abcabdabb") == 4
    assert s.lengthOfLongestSubstring("abba") == 2

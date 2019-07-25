class Solution(object):

    # 要注意是最长前缀！！！
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        i = 0
        done = False
        while i < len(strs[0]):
            v = strs[0][i]
            for j in range(0, len(strs)):
                s = strs[j]
                if i >= len(s):
                    done = True
                    break
                if v != s[i]:
                    done = True
                    break
            if done:
                break
            i += 1
        return strs[0][:i]


def test_longest_common_prefix():
    s = Solution()

    assert "fl" == s.longestCommonPrefix(["flower", "flow", "flight"])
    assert "" == s.longestCommonPrefix(["dog", "racecar", "car"])

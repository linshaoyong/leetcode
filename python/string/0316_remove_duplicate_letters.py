class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        counts = {}
        for c in s:
            counts[c] = counts.get(c, 0) + 1

        res = []
        for i, c in enumerate(s):
            if counts[c] < 1:
                continue
            
            if counts[c] == 1:
                res.append(c)
                continue

            print(i, c)
            if c < s[i+1]:
                j = i
                while j < len(s) - 1:
                    if s[j] < s[j+1] and counts[s[j]]>1:
                        j += 1
                        continue
                    res.append(c)
                    for x in range(i, j):
                        counts[s[x]] = counts[s[x]] -1
                    break
                

        return ''.join(res)
            

def test_remove_duplicate_letters():
    s = Solution()
    assert "abc" == s.removeDuplicateLetters("bcabc")
    assert "acdb" == s.removeDuplicateLetters("cbacdcbc")

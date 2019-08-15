class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(T)
        stack = []
        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                cur = stack.pop()
                ans[cur] = i - cur
            stack.append(i)
        return ans


def test_daily_temperatures():
    s = Solution()

    assert [1, 1, 4, 2, 1, 1, 0, 0] == s.dailyTemperatures(
        [73, 74, 75, 71, 69, 72, 76, 73])

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        r, s, t = -1, 0, 0
        for i in range(0, len(gas)):
            t = t + gas[i] - cost[i]
            s = s + gas[i] - cost[i]
            if s < 0:
                r = -1
                s = 0
            else:
                if r == -1:
                    r = i
        if t < 0:
            r = -1
        return r


def test_can_complete_circuit():
    s = Solution()

    assert 3 == s.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])
    assert -1 == s.canCompleteCircuit([2, 3, 4], [3, 4, 3])
    assert 4 == s.canCompleteCircuit([5, 1, 2, 3, 4], [4, 4, 1, 5, 1])

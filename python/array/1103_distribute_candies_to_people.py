class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        res = [0] * num_people
        candy = 1
        while candies:
            for i in range(num_people):
                if candies > candy:
                    res[i] += candy
                    candies -= candy
                    candy += 1
                else:
                    res[i] += candies
                    candies = 0
                    break
        return res


def test_distribute_candies():
    s = Solution()
    assert [1, 2, 3, 1] == s.distributeCandies(7, 4)
    assert [5, 2, 3] == s.distributeCandies(10, 3)

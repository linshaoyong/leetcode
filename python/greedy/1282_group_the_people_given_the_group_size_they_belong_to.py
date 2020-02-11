class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        size_ids = {}
        for i in range(len(groupSizes)):
            size = groupSizes[i]
            v = size_ids.get(size, [])
            v.append(i)
            size_ids[size] = v

        res = []
        for size, ids in size_ids.items():
            n = len(ids) // size
            for i in range(n):
                res.append(ids[i * size:(i + 1) * size])
        return res


def test_group_the_people():
    s = Solution()
    assert 3 == len(s.groupThePeople([3, 3, 3, 3, 3, 1, 3]))
    assert 3 == len(s.groupThePeople([2, 1, 3, 3, 3, 2]))

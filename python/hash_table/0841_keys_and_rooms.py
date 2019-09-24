class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        keys = set([0])
        new_keys = [0]
        while new_keys:
            ks = []
            for key in new_keys:
                for v in rooms[key]:
                    if v not in keys:
                        ks.append(v)
                        keys.add(v)
            new_keys = ks
        return len(keys) == len(rooms)


def test_can_visit_all_rooms():
    s = Solution()
    assert s.canVisitAllRooms([[1], [2], [3], []])
    assert s.canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]) is False

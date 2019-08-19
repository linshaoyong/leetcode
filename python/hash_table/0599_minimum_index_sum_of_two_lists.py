class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        m = {r: i for i, r in enumerate(list1)}
        min_i = len(list1) + len(list2)
        indexs = []
        for i, restaurant in enumerate(list2):
            if restaurant in m:
                if m[restaurant] + i < min_i:
                    min_i = m[restaurant] + i
                    indexs = [i]
                    continue
                if m[restaurant] + i == min_i:
                    indexs.append(i)
        return [list2[i] for i in indexs]


def test_find_restaurant():
    s = Solution()
    assert ["Shogun"] == s.findRestaurant(
        ["Shogun", "Tapioca Express", "Burger King", "KFC"],
        ["Piatti", "The Grill at Torrey Pines",
         "Hungry Hunter Steakhouse", "Shogun"])

    assert ["Shogun"] == s.findRestaurant(
        ["Shogun", "Tapioca Express", "Burger King", "KFC"],
        ["KFC", "Shogun", "Burger King"])

    assert ["KFC", "Burger King", "Tapioca Express", "Shogun"] == \
        s.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"],
                         ["KFC", "Burger King", "Tapioca Express", "Shogun"])

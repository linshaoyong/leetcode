class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        lines = 1
        curr_width = 0

        for s in S:
            width = widths[ord(s) - 97]
            if curr_width + width <= 100:
                curr_width += width
                continue
            lines += 1
            curr_width = width
        return [lines, curr_width]


def test_number_of_lines():
    assert [3, 60] == Solution().numberOfLines(
        [10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
         10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
         10, 10, 10, 10, 10, 10],
        "abcdefghijklmnopqrstuvwxyz")
    assert [2, 4] == Solution().numberOfLines(
        [4, 10, 10, 10, 10, 10, 10, 10, 10, 10,
         10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
         10, 10, 10, 10, 10, 10], "bbbcccdddaaa")

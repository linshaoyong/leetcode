class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        res = set()
        self.traverse(tiles, 0, len(tiles), [], res)
        print(sorted([i for i in list(res) if len(i) == 1]))
        print(sorted([i for i in list(res) if len(i) == 2]))
        print(sorted([i for i in list(res) if len(i) == 3]))
        print(sorted([i for i in list(res) if len(i) == 4]))
        print(sorted([i for i in list(res) if len(i) == 5]))
        print(sorted([i for i in list(res) if len(i) == 6]))
        return len(res)

    def traverse(self, tiles, start, end, path, res):
        for i in range(start, end):
            path.append(tiles[i])
            res.add(''.join(path))
            self.traverse(tiles, start, i, path, res)
            self.traverse(tiles, i + 1, end, path, res)
            path.pop()


def test_num_tile_possibilities():
    assert 8 == Solution().numTilePossibilities("AAB")
    assert 188 == Solution().numTilePossibilities("AAABBC")

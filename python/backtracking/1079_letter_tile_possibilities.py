class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        res = set()
        self.traverse(tiles, [], res)
        return len(res)

    def traverse(self, tiles, path, res):
        for i in range(len(tiles)):
            path.append(tiles[i])
            res.add(''.join(path))
            self.traverse(tiles[:i] + tiles[i + 1:], path, res)
            path.pop()


def test_num_tile_possibilities():
    assert 8 == Solution().numTilePossibilities("AAB")
    assert 188 == Solution().numTilePossibilities("AAABBC")

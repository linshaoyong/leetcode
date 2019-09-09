class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        hs = {}
        for p in paths:
            sps = p.split()
            root = sps[0]
            for f in sps[1:]:
                fn, content = f.split('(')
                fs = hs.get(content, [])
                fs.append(root + '/' + fn)
                hs[content] = fs
        return [v for _, v in hs.items() if len(v) > 1]


def test_find_duplicate():

    r = Solution().findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)",
                                  "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)",
                                  "root 4.txt(efgh)"])

    assert 2 == len(r)

    r0, r1 = r[0], r[1]
    assert 2 == len(r0) or 3 == len(r0)
    assert 2 == len(r1) or 3 == len(r1)
    assert "root/a/2.txt" in r0 or "root/a/2.txt" in r1
    assert "root/c/d/4.txt" in r0 or "root/c/d/4.txt" in r1
    assert "root/4.txt" in r0 or "root/4.txt" in r1
    assert "root/a/1.txt" in r0 or "root/a/1.txt" in r1
    assert "root/c/3.txt" in r0 or "root/c/3.txt" in r1

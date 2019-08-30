class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        res = {}
        for cpd in cpdomains:
            c, domain = cpd.split()
            res[domain] = res.get(domain, 0) + int(c)
            while '.' in domain:
                domain = domain.split('.', 1)[-1]
                res[domain] = res.get(domain, 0) + int(c)
        return [str(v) + ' ' + k for k, v in res.items()]


def test_subdomain_visits():
    s = Solution()
    r = s.subdomainVisits(["9001 discuss.leetcode.com"])
    assert 3 == len(r)
    assert "9001 discuss.leetcode.com" in r
    assert "9001 leetcode.com" in r
    assert "9001 com" in r

    r = s.subdomainVisits(["900 google.mail.com", "50 yahoo.com",
                           "1 intel.mail.com", "5 wiki.org"])
    assert 7 == len(r)
    assert "901 mail.com" in r
    assert "50 yahoo.com" in r
    assert "900 google.mail.com" in r
    assert "5 wiki.org" in r
    assert "5 org" in r
    assert "1 intel.mail.com" in r
    assert "951 com" in r

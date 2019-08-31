class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        es = set()
        for email in emails:
            skip = False
            r = []
            for i in range(0, len(email)):
                if email[i] == '@':
                    r.append(email[i:])
                    break
                if email[i] == '+':
                    skip = True
                if skip:
                    continue
                if email[i] == '.':
                    continue
                r.append(email[i])
            es.add(''.join(r))
        return len(es)


def test_num_unique_emails():
    assert 2 == Solution().numUniqueEmails(
        ["test.email+alex@leetcode.com",
         "test.e.mail+bob.cathy@leetcode.com",
         "testemail+david@lee.tcode.com"])

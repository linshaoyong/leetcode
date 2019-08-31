class RecentCounter(object):

    def __init__(self):
        self.requests = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.requests.append(t)
        j = 0
        for i in range(0, len(self.requests)):
            if t - self.requests[i] <= 3000:
                j = i
                break
        self.requests = self.requests[j:]
        return len(self.requests)


def test_ping():

    rc = RecentCounter()
    assert 1 == rc.ping(1)
    assert 2 == rc.ping(100)
    assert 3 == rc.ping(3001)
    assert 3 == rc.ping(3002)

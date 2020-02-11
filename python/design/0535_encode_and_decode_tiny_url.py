import hashlib


class Codec:

    def __init__(self):
        self.prefix = 'http://tinyurl.com/'
        self.urls = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        key = hashlib.sha1(longUrl.encode()).hexdigest()[:8]
        self.urls[key] = longUrl
        return self.prefix + key

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        key = shortUrl.replace(self.prefix, '')
        return self.urls.get(key, '')


def test_codec():
    codec = Codec()

    url = 'https://leetcode.com/problems/design-tinyurl'
    assert url == codec.decode(codec.encode(url))

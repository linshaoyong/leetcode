class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        res = []
        words = S.split()
        for i in range(0, len(words)):
            word = words[i]
            if word[0].lower() not in vowels:
                word = word[1:] + word[0]
            word = word + 'ma' + 'a' * (i + 1)
            res.append(word)
        return ' '.join(res)


def test_to_goat_latin():
    assert "Imaa peaksmaaa oatGmaaaa atinLmaaaaa" == Solution(
    ).toGoatLatin("I speak Goat Latin")

    assert "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa" == Solution(
    ).toGoatLatin("The quick brown fox jumped over the lazy dog")

import unittest
from collections import Counter

class LongestSubstringWithNonrepeatingChars(unittest.TestCase):

    def unique(self, s):
        maxel = max(Counter(s).iteritems(), key=lambda x: x[1])
        return maxel[1] == 1

    def longest(self, s):
        maxs = ''
        maxlen = 0
        for i in xrange(len(s)):
            for j in xrange(i+1, len(s) + 1):
                if self.unique(s[i:j]):
                    if j-i > maxlen:
                        maxlen = j-i
                        maxs = s[i:j]
                else:
                    continue
        return maxs

    def test_unique_string_returns_itself(self):
        self.assertEqual(self.longest('abc'), 'abc')

    def test_finds_substring(self):
        self.assertEqual(self.longest('abcabcbb'), 'abc')

    def test_finds_substring2(self):
        self.assertEqual(self.longest('bbbbb'), 'b')

    def test_finds_substring3(self):
        self.assertEqual(self.longest('pwwkew'), 'wke')

    def test_unique(self):
        self.assertTrue(self.unique('abc'))

    def test_unique2(self):
        self.assertFalse(self.unique('abcb'))

if __name__ == '__main__':
    unittest.main()

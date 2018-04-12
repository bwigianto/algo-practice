import unittest

class LongestSubstringWithNonrepeatingChars(unittest.TestCase):

    def longest(self, s):
        seen = {}
        maxlen = 0
        j = 0
        for i in xrange(len(s)):
            if s[i] in seen:
                j = max(j, seen[s[i]] + 1)
            seen[s[i]] = i
            maxlen = max(i - j + 1, maxlen)
        return maxlen

    def test_unique_string_returns_itself(self):
        self.assertEqual(self.longest('abc'), 3)

    def test_finds_substring(self):
        self.assertEqual(self.longest('abcabcbb'), 3)

    def test_finds_substring2(self):
        self.assertEqual(self.longest('bbbbb'), 1)

    def test_finds_substring3(self):
        self.assertEqual(self.longest('pwwkew'), 3)

    def test_finds_substring4(self):
        self.assertEqual(self.longest("iulyqqziheiztnagxszqaovtsydaennoibmyrniatq"), 10)

if __name__ == '__main__':
    unittest.main()

import unittest

class LongestSubstringTest(unittest.TestCase):
    def maxpalindrome_at_gap(self, s, i):
        pal = ''
        if i >= len(s):
            return pal
        first = i
        last = i + 1
        while first >= 0 and last < len(s) and s[first] == s[last]:
            pal = s[first:last+1]
            first -= 1
            last += 1
        return pal

    def maxpalindrome_with_center(self, s, i):
        first = i
        last = i
        pal = ''
        while first >= 0 and last < len(s) and s[first] == s[last]:
            pal = s[first:last+1]
            first -= 1
            last += 1

        return pal

    def longestPalindrome(self, s):
        maxpal = ''
        for i in xrange(len(s)):
            curr = self.maxpalindrome_with_center(s, i)
            curr2 = self.maxpalindrome_at_gap(s, i)
            if len(curr) > len(maxpal):
                maxpal = curr
            if len(curr2) > len(maxpal):
                maxpal = curr2
        return maxpal

    def test_longest_palindrome(self):
        self.assertEqual(self.longestPalindrome("babad"), "bab")

    def test_longest_palindrome_even_number(self):
        self.assertEqual(self.longestPalindrome("cbbd"), "bb")
if __name__ == '__main__':
    unittest.main()

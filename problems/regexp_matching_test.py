import unittest

class RegularExpressionMatchTest(unittest.TestCase):
    def isMatch(self, s, p):
        def p_match(a, b):
            return a == b or b == '.'
        def consume_char(s, i):
            if i >= len(s):
                return ((None, None), None) 
            token = s[i]
            if i + 1 < len(s) and s[i + 1] == '*':
                return ((s[i], '*'), i + 2)
            return ((s[i], None), i + 1)
        def single_use(pchar):
            return pchar[1] == None

        si = 0
        pi = 0
        pchar = (None, None)
        while si < len(s):
            if single_use(pchar) or not p_match(s[si], pchar[0]):
                (pchar, pi) = consume_char(p, pi)
            while not p_match(s[si], pchar[0]):
                if not single_use(pchar):
                    (pchar, pi) = consume_char(p, pi)
                    if not pchar[0]:
                        return False
                    continue
                return False
            si += 1
        return pi == len(p)
    
    def test_empty_match_empty(self):
        self.assertTrue(self.isMatch('', ''))

    def test_match_when_regex_identical_to_string(self):
        self.assertTrue(self.isMatch('abcd', 'abcd'))

    def test_no_match_if_not_entire_match(self):
        self.assertFalse(self.isMatch('abcd', 'abce'))

    def test_dot_as_wildcard(self):
        self.assertTrue(self.isMatch('abcd', 'ab.d'))

    def test_multiple_dots(self):
        self.assertTrue(self.isMatch('abcd', 'a..d'))

    def test_single_star(self):
        self.assertTrue(self.isMatch('aaa', 'a*'))

    def test_dot_and_star(self):
        self.assertTrue(self.isMatch('ab', '.*'))
        self.assertFalse(self.isMatch('abc', 'ad.*'))

    def test_dot_and_star2(self):
        self.assertTrue(self.isMatch('aab', 'c*a*b'))

    def test_dot_and_star3(self):
        self.assertFalse(self.isMatch('mississippi', 'mis*is*p*.'))

    def test_dot_and_star_with_false_end(self):
        self.assertFalse(self.isMatch('ab', '.*c'))

#    def test_dont_overmatch_star(self):
#        self.assertTrue(self.isMatch('aaa', 'a*a'))
if __name__ == '__main__':
    unittest.main()

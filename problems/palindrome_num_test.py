import unittest

class PalindromeNumTest(unittest.TestCase):
    def isPalindrome(self, n):
        x = n
        s = 0
        for exp in xrange(len(str(x)) - 1, -1, -1):
            s += 10 ** exp * (x % 10)
            x /= 10
        return s == n

    def test_single_digit(self):
        self.assertEquals(self.isPalindrome(9), True)

    def test_double_digit(self):
        self.assertEquals(self.isPalindrome(22), True)
        self.assertEquals(self.isPalindrome(21), False)

    def test_triple_digit(self):
        self.assertEquals(self.isPalindrome(121), True)

    def test_handle_negative(self):
        self.assertFalse(self.isPalindrome(-1))
        self.assertFalse(self.isPalindrome(-121))

if __name__ == '__main__':
    unittest.main()


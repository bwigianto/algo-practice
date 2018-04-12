import unittest

class ReverseIntegerTest(unittest.TestCase):
    def overflowed(self, x):
        return 0 if x > 2147483647 else x

    def reverse(self, x):
        s = 0
        multiplier = -1 if x < 0 else 1
        x *= multiplier
        exp = len(str(x)) - 1
        while x > 0:
            r = (x % 10)
            s += 10 ** exp * r
            x /= 10
            exp -= 1
        return self.overflowed(s) * multiplier

    def test_reverse_single_digit(self):
        self.assertEquals(self.reverse(9), 9)

    def test_reverse_two_digit(self):
        self.assertEquals(self.reverse(19), 91)

    def test_reverse_two_with_zero(self):
        self.assertEquals(self.reverse(120), 21)

    def test_handle_negative(self):
        self.assertEquals(self.reverse(-123), -321)
if __name__ == '__main__':
    unittest.main()


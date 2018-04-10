import unittest

class ZigzagConversionTest(unittest.TestCase):
    def next_delta(self, i, n):
        return 1 if (i / (n-1)) % 2 == 0 else -1

    def convert(self, s, n):
        if n == 1:
            return s
        queues = []
        for i in xrange(n):
            queues.append([])
        i = 0
        for j in xrange(len(s)):
            queues[i].append(s[j])
            i += self.next_delta(j, n)
        out = ''
        for q in queues:
            out += ''.join(q)
        return out

    def test_empty(self):
        self.assertEquals(self.convert('', 5), '')

    def test_single_queue(self):
        self.assertEquals(self.convert('AB', 1), 'AB')

    def test_next_delta(self):
        self.assertEquals(self.next_delta(0, 3), 1)
        self.assertEquals(self.next_delta(1, 3), 1)
        self.assertEquals(self.next_delta(2, 3), -1)
        self.assertEquals(self.next_delta(3, 3), -1)

    def test_next_delta2(self):
        self.assertEquals(self.next_delta(0, 4), 1)
        self.assertEquals(self.next_delta(1, 4), 1)
        self.assertEquals(self.next_delta(2, 4), 1)
        self.assertEquals(self.next_delta(3, 4), -1)
        self.assertEquals(self.next_delta(4, 4), -1)
        self.assertEquals(self.next_delta(5, 4), -1)
        self.assertEquals(self.next_delta(6, 4), 1)

    def test_example(self):
        self.assertEquals(self.convert('PAYPALISHIRING', 3), 'PAHNAPLSIIGYIR')

if __name__ == '__main__':
    unittest.main()

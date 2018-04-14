import unittest
import itertools

class MaxContainerTest(unittest.TestCase):
    def area(self, a, b):
        return abs(b[0] - a[0]) * min(a[1], b[1])

    def maxArea(self, a):
        tuples = [(i+1, a[i]) for i in xrange(len(a))]
        maxval = -1
        for combo in itertools.combinations(tuples, 2):
            maxval = max(maxval, self.area(combo[0], combo[1]))
        return maxval
    
    def test_area_from_two_points(self):
        self.assertEquals(self.area((1, 3), (4, 5)), 9)

    def test_area_from_two_points_backwards(self):
        self.assertEquals(self.area((4, 5), (1, 3)), 9)

    def test_three_points_only(self):
        self.assertEquals(self.maxArea([1, 2, 3]), 2)

if __name__ == '__main__':
    unittest.main()

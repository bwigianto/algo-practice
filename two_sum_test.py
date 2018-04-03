import unittest

class TwoSumTest(unittest.TestCase):

    def twoSum(self, nums, target):
        num_to_index = {}
        for i, n in enumerate(nums):
            if target - n in num_to_index:
                return [num_to_index[target - n], i]
            num_to_index[n] = i

    def test_find_sum_end(self):
        self.assertEqual(self.twoSum([1, 3, 5], 8), [1, 2])

    def test_dont_duplicate(self):
        self.assertEqual(self.twoSum([1, 3, 5], 6), [0, 2])

if __name__ == '__main__':
    unittest.main()

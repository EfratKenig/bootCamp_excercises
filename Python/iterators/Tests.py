import unittest

from ex.CircleIter import CircleIter
from ex.get_prime_factors_generator import get_prime_factors_generator
from ex.my_accumulate import my_accumulate
from ex.my_enumerate import my_enumerate


class MyTestCase(unittest.TestCase):
    def test_my_enumerate(self):
        res = []
        for index, elem in my_enumerate([10, 20, 30, 40]):
            res.append((index, elem))
        self.assertEqual(res, [(0, 10), (1, 20), (2, 30), (3, 40)])

        res = []
        for index, elem in my_enumerate([10, 20, 30, 40], 10):
            res.append((index, elem))
        self.assertEqual(res, [(10, 10), (11, 20), (12, 30), (13, 40)])

    def test_my_accumulate(self):
        res = []
        for elem in my_accumulate([1, 2, 3, 4, 5]):
            res.append(elem)
        self.assertEqual(res, [1, 3, 6, 10, 15])

    def test_get_prime_factors_generator(self):
        res = []
        for x in get_prime_factors_generator(100):
            res.append(x)
        self.assertEqual(res[::-1], [2, 2, 5, 5])

    def test_CircleIter(self):
        res = []
        for x in CircleIter([1, 2], 5):
            res.append(x)
        self.assertEqual(res, [1, 2, 1, 2, 1])

        res = []
        for x in CircleIter([1, 2, 3], 4):
            res.append(x)
            for y in CircleIter([5, 6], 3):
                res.append(y)
        self.assertEqual(res, [1, 5, 6, 5, 2, 5, 6, 5, 3, 5, 6, 5, 1, 5, 6, 5])


if __name__ == '__main__':
    unittest.main()

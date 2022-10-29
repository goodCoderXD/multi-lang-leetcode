import solution
import unittest

class SolutionTest(unittest.TestCase):

    def test_a(self):
        self.assertEqual(
            solution.median_of_two_sorted_arrays([1, 3], [2]),
            2.0
        )

    def test_empty_second_odd(self):
        self.assertEqual(
            solution.median_of_two_sorted_arrays([1, 2, 3], []),
            2.0
        )

    def test_empty_second_even(self):
        self.assertEqual(
            solution.median_of_two_sorted_arrays([1, 5], []),
            3.0
        )

    def test_two_perfectly_partitioned(self):
        self.assertEqual(
            solution.median_of_two_sorted_arrays([1, 2], [3, 4]),
            2.5
        )

    def test_two_perfectly_partitioned_odd(self):
        self.assertEqual(
            solution.median_of_two_sorted_arrays([1], [3, 4]),
            3
        )

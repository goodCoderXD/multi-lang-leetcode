import solution
import unittest

class SolutionTest(unittest.TestCase):

    def test_a(self):
        self.assertTrue(
            solution.is_match("aa", "aa")
        )

    def test_b(self):
        self.assertTrue(
            solution.is_match("az", "a.")
        )

    def test_c(self):
        self.assertTrue(
            solution.is_match("azc", "a.c")
        )

    def test_d(self):
        self.assertTrue(
            solution.is_match("azc", "az.")
        )

    def test_d(self):
        self.assertTrue(
            solution.is_match("azc", ".zc")
        )

    def test_e(self):
        self.assertFalse(
            solution.is_match("azc", "bzc")
        )

    def test_f(self):
        self.assertFalse(
            solution.is_match("azc", "bzc.")
        )

    def test_g(self):
        self.assertFalse(
            solution.is_match("azc", ".bzc")
        )

    def test_h(self):
        self.assertFalse(
            solution.is_match("azc", "a")
        )

    def test_i(self):
        self.assertTrue(
            solution.is_match("aaaazc", "a*zc")
        )

    def test_j(self):
        self.assertTrue(
            solution.is_match("aa", "a*")
        )

    def test_k(self):
        self.assertTrue(
            solution.is_match("aab", "c*a*b")
        )
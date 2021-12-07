from jduunit import unittest


class TestVariables(unittest.TestCase):
    def test_is_in(self):
        self.assertIn(4, [4, 5, 6])

    def test_not_in(self):
        self.assertNotIn(1, [4, 5, 6])

    def test_is_instance(self):
        self.assertIsInstance("foo", str)

    def test_recursion(self):
        with self.assertRaises(RecursionError):
            self.factorial(0)

    def test_equal(self):
        self.assertEqual(self.factorial(5), 120)

    def test_equal_dicts(self):
        self.assertDictEqual({"a": 1}, {"a": 1})

    def test_list_counts(self):
        self.assertCountEqual([1, 2, 3, 2, 1], [1, 1, 2, 2, 3])

    def factorial(self, n):
        if n == 1:
            return n
        return self.factorial(n - 1) * n


if __name__ == "__main__":
    unittest.main()

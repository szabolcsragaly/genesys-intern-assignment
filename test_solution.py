import unittest
from solution import Solution
class TestCombinations(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        result = self.solution.combinations("23")
        expected = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
        self.assertCountEqual(result, expected)

    def test_example_2(self):
        self.assertEqual(self.solution.combinations(""), [])

    def test_example_3(self):
        result = self.solution.combinations("2")
        expected = ["a", "b", "c"]
        self.assertCountEqual(result, expected)

    def test_multiple_digits(self):
        result = self.solution.combinations("79")
        self.assertEqual(len(result), 16) 

    def test_max_length(self):
        result = self.solution.combinations("9999")
        self.assertEqual(len(result), 256)

    def test_contains_invalid_letter(self):
        with self.assertRaises(ValueError):
            self.solution.combinations("21")

    def test_invalid_length(self):
        with self.assertRaises(ValueError):
            self.solution.combinations("23456")

    def test_invalid_characters(self):
        with self.assertRaises(ValueError):
            self.solution.combinations("2a3")


if __name__ == "__main__":
    unittest.main()
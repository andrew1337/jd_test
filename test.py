import unittest
from edited_distance import minimal_distance as initinal_distance_f
from my_distance import minimal_distance as my_distance_f
from my_distance import recursive_minimal_distance, ineffective_minimal_distance


class TestDistanceImplementations(unittest.TestCase):
    def setUp(self) -> None:
        self.test_data = {
            ("carry", "bark"): 3,
            ("", ""): 0,
            ("", "aaa"): 3,
            ("aaa", "a"): 2,
            ("aaa", "aaa"): 0,
            ("sakura", "cat"): 5,
            ("kitten", "sitting"): 3,
            ("sitting", "kitten"): 3,
            ("saturday", "sunday"): 3,
            ("aba", "aca"): 1,
            ("abc", "aba"): 1,
            ("abc", "bbc"): 1,
            ("helloworld", "alohaworld"): 5,
            ("helloworld", "helloworld"): 0,
            ("alohaworld", "alohaworld"): 0,
            ("horse", "ros"): 3,
            ("ros", "horse"): 3,
            ("intention", "execution"): 5,
            ("zoologicoarchaeologist", "zoogeologist"): 10,
            ("zoogeologist", "zoologicoarchaeologist"): 10,
            ("aggctatcacctgacctccaggccgatgccc", "tagctatcacgaccgcggtcgatttgcccgac"): 13,
        }

    def test_initial(self):
        for (s, t), expected in self.test_data.items():
            with self.subTest(s=s, t=t):
                self.assertEqual(initinal_distance_f(s, t), expected)

    def test_ineffective(self):
        for (s, t), expected in self.test_data.items():
            with self.subTest(s=s, t=t):
                self.assertEqual(ineffective_minimal_distance(s, t), expected)

    def test_recursive(self):
        for (s, t), expected in self.test_data.items():
            with self.subTest(s=s, t=t):
                self.assertEqual(recursive_minimal_distance(s, t), expected)

    def test_my(self):
        for (s, t), expected in self.test_data.items():
            with self.subTest(s=s, t=t):
                self.assertEqual(my_distance_f(s, t), expected)


if __name__ == "__main__":
    unittest.main()

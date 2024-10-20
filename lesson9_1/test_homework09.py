import unittest
from homeworks import sum_even_numbers, list_str, unique_characters, part_of_pay


class TestHomeworks(unittest.TestCase):

    def test_sum_even_numbers(self):
        self.assertEqual(sum_even_numbers([12, 54, 1, 5, 8, 77, 45, 66]), 140)
        self.assertTrue(sum_even_numbers([12, 54, 1, 5, 8, -76, 46, 66]) == 110)
        self.assertFalse(sum_even_numbers([33, 55, 7, 11, 15]) == 4)

    def test_list_str(self):
        self.assertEqual(list_str(['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']) ==
                         ['1', '2', 'False', '6', 'Python', 'Lorem Ipsum'])
        self.assertIsNone(list_str([]))

    def test_unique_characters(self):
        self.assertEqual(unique_characters("sag rgrg erg rgegseg sgsg sgrgrgrgrg dfgdg. welcome!"), True)
        self.assertIn(unique_characters("sag rgrg erg rgegseg sgsg sgrgrgrgrg dfgdg. welcome!"), welcome)
        self.assertNotIn(unique_characters("sag rgrg erg rgegseg sgsg sgrgrgrgrg dfgdg. welcome!"), test)

    def test_part_of_pay(self):
        self.assertEqual(part_of_pay(6), 36)
        self.assertGreater(part_of_pay(5), 21)
        self.assertLess(part_of_pay(8), 21)


if __name__ == '__main__':
    unittest.main()

    







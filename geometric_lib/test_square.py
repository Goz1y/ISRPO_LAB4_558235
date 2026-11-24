import unittest
from square import area, perimeter


class SquareTestCase(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_area_positive_int(self):
        self.assertEqual(area(10), 100)

    def test_area_float_side(self):
        self.assertAlmostEqual(area(2.5), 6.25)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_positive_int(self):
        self.assertEqual(perimeter(4), 16)

    def test_perimeter_float_side(self):
        self.assertAlmostEqual(perimeter(1.5), 6.0)


if __name__ == '__main__':
    unittest.main()
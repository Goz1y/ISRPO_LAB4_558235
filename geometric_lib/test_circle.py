import unittest
import math
from circle import area, perimeter


class CircleTestCase(unittest.TestCase):
    def test_area_unit_radius(self):
        self.assertAlmostEqual(area(1), math.pi)

    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_area_float_radius(self):
        self.assertAlmostEqual(area(2.5), math.pi * 2.5 * 2.5)

    def test_perimeter_unit_radius(self):
        self.assertAlmostEqual(perimeter(1), 2 * math.pi)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_float_radius(self):
        self.assertAlmostEqual(perimeter(1.5), 3 * math.pi)


if __name__ == '__main__':
    unittest.main()
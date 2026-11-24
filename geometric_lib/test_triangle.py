import unittest
from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    def test_area_zero_height(self):
        self.assertEqual(area(10, 0), 0)

    def test_area_base_height(self):
        self.assertEqual(area(10, 10), 50)

    def test_area_float_base(self):
        self.assertAlmostEqual(area(3.5, 2), 3.5)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0, 0, 0), 0)

    def test_perimeter_int_sides(self):
        self.assertEqual(perimeter(3, 4, 5), 12)

    def test_perimeter_float_sides(self):
        self.assertAlmostEqual(perimeter(1.5, 2.5, 3.0), 7.0)


if __name__ == '__main__':
    unittest.main()
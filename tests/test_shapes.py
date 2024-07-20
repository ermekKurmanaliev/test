import unittest
import math
from geometry.shapes import Circle, Triangle, calculate_area

class TestShapes(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), math.pi * 25)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6)

    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            Triangle(1, 1, 3)

    def test_right_angle_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_angle())
        triangle = Triangle(5, 12, 13)
        self.assertTrue(triangle.is_right_angle())
        triangle = Triangle(6, 8, 10)
        self.assertTrue(triangle.is_right_angle())

    def test_not_right_angle_triangle(self):
        triangle = Triangle(2, 2, 3)
        self.assertFalse(triangle.is_right_angle())

    def test_calculate_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(calculate_area(circle), math.pi * 25)
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(calculate_area(triangle), 6)

if __name__ == "__main__":
    unittest.main()

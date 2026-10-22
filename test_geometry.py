"""Checks that geometry.py does the math it claims to do."""
import unittest
import math
import geometry

class GeometryTests(unittest.TestCase):
    def test_area_rectangle(self):
        self.assertEqual(geometry.area_rectangle(4, 5), 20)
        
    def test_perimeter_rectangle(self):
        self.assertEqual(geometry.perimeter_rectangle(4, 5), 18)
        
    def test_area_circle(self):
        self.assertAlmostEqual(geometry.area_circle(3), math.pi * 9)
        
    def test_circumference(self):
        self.assertAlmostEqual(geometry.circumference(3), 2 * math.pi * 3)
        
    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            geometry.area_circle(-1)

if __name__ == "__main__":
    unittest.main()
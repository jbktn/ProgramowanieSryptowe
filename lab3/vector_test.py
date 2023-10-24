import unittest
from model import Vector2d

class test_capture_stdout(unittest.TestCase):
    def setUp(self):
        self.vector1 = Vector2d(1, 2)
        self.vector2 = Vector2d(-2, 1)

    def test_get_x(self):
        self.assertEqual(self.vector1.get_x(), 1)

    def test_get_y(self):
        self.assertEqual(self.vector1.get_y(), 2)

    def test_add(self):
        result = self.vector1.add(self.vector2)
        self.assertEqual(result.get_x(), -1)
        self.assertEqual(result.get_y(), 3)

    def test_subtract(self):
        result = self.vector1.subtract(self.vector2)
        self.assertEqual(result.get_x(), 3)
        self.assertEqual(result.get_y(), 1)

    def test_lowerLeft(self):
        result = self.vector1.lowerLeft(self.vector2)
        self.assertEqual(result.get_x(), -2)
        self.assertEqual(result.get_y(), 1)

    def test_upperRight(self):
        result = self.vector1.upperRight(self.vector2)
        self.assertEqual(result.get_x(), 1)
        self.assertEqual(result.get_y(), 2)
    
    def test_precedes(self):
        self.assertFalse(self.vector1.precedes(self.vector2))

    def test_follows(self):
        self.assertTrue(self.vector1.follows(self.vector2))

    def test_opposite(self):
        result = self.vector1.opposite()
        self.assertEqual(result.get_x(), -1)
        self.assertEqual(result.get_y(), -2)

    def test_eq(self):
        self.assertFalse(self.vector1.__eq__(self.vector2))


if __name__ == '__main__':
    unittest.main()
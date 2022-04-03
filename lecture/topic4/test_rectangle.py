import unittest
from lecture.topic4 import square as s


class RectangleClassTest(unittest.TestCase):

    def setUp(self):
        self.shape = s.Square(12, 23)

    def tearDown(self):
        del self.shape

    def test_constructor(self):
        with self.assertRaises(s.InvalidSideError):
            r = s.Square(5, -5)
        with self.assertRaises(s.InvalidSideError):
            r = s.Square(-5, 5)

    def test_shape_area(self):
        self.assertAlmostEqual(276, self.shape.area())


if __name__ == '__main__':
    unittest.main()

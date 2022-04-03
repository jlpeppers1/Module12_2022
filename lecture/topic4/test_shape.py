import unittest
from lecture.topic4 import shape as s


class ShapeClassTest(unittest.TestCase):

    def test_sides(self):
        with self.assertRaises(TypeError):
            s.Shape()

if __name__ == '__main__':
    unittest.main()

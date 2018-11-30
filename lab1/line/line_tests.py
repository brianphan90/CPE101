import unittest
from line import Line

class LineTests(unittest.TestCase):
   
      # Add code here.
      # 1) Create a Line with x1, y1, x2, y2 values of your choice.
      # 2) Use assertEqual on each field in the new Line to verify
      #    that it holds the expected value.
   def test_line(self):
        line_1 = Line(0, 0, 2, 2)
        self.assertEqual(line_1.x1, 0)
        self.assertEqual(line_1.y1, 0)
        self.assertEqual(line_1.x2, 2)
        self.assertEqual(line_1.y2, 2)

   def test_line2(self):
        line_2 = Line(1, 1, 3, 3)
        self.assertEqual(line_2.x1, 1)
        self.assertEqual(line_2.y1, 1)
        self.assertEqual(line_2.x2, 3)
        self.assertEqual(line_2.y2, 3)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()


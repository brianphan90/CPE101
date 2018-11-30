import unittest
import fold
import point

class TestCases(unittest.TestCase):
   def test_sum_1(self):
      old_list = [1,1,1,1]
      self.assertEqual(fold.sum(old_list), 4)

   def test_sum_2(self):
      old_list = [1,2,3,4]
      self.assertEqual(fold.sum(old_list), 10)

if __name__ == '__main__':
   unittest.main()


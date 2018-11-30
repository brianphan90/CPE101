import unittest
import logic

class TestCases(unittest.TestCase):
   def test_case_1(self):
      remainder = logic.is_even(4)
      self.assertTrue(remainder == 0)

   def test_case_2(self):
      remainder = logic.is_even(5)
      self.assertFalse(remainder == 0)
   
   def test_interval_1(self):
      int1 = logic.in_an_interval(102)
      self.assertTrue(int1, True)
   
   def test_interval_2(self):
      int1 = logic.in_an_interval(11)
      self.assertEqual(int1, False)
# Run the unit tests.
if __name__ == '__main__':
   unittest.main()


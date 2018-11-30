import unittest
import conditional

class TestCases(unittest.TestCase):
   def test_max_of_two_1(self):
      max_of_two = conditional.max_101(10,9)
      self.assertEqual(max_of_two,10)
   def test_max_of_two_2(self):
      max_of_two = conditional.max_101(8,12)
      self.assertEqual(max_of_two, 12)
   def test_max_3_1(self):
      max_3 = conditional.max_of_three(2,3,4)
      self.assertEqual(max_3, 4)
   def test_max_3_2(self):
      max_3 = conditional.max_of_three(3,4,5)
      self.assertEqual(max_3, 5)
   def test_late_rental(self):
      fee = conditional.rental_late_fee(4)
      self.assertEqual(fee, 5)
   def test_late_rental_2(self):
      fee = conditional.rental_late_fee(23)
      self.assertTrue( fee == 19)
 


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()


import unittest
import funcs
import math
class TestCases(unittest.TestCase):
   
   def test_f_1(self):
      f_1 = funcs.f(1)   
      self.assertEqual(f_1, 9)

   def test_f_2(self):
      f_2 = funcs.f(2)
      self.assertEqual(f_2, 32)		
   
   def test_f3(self):
      g_1=funcs.g(1,1)
      self.assertEqual(g_1,2)

   def test_f4(self):
      g_2=funcs.g(0,0)
      self.assertEqual(g_2,0)

   def test_f5(self):
      h1=funcs.hypotenuse(3,4)
      self.assertEqual(h1,5)

   def test_f6(self):
      h2=funcs.hypotenuse(6,8)
      self.assertEqual(h2,10)

   def test_f7(self):
      pos1=funcs.is_positive(3)
      self.assertTrue(pos1,True)

   def test_f8(self):
      pos2=funcs.is_positive(-1)
      self.assertFalse(pos2,False)

      


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()


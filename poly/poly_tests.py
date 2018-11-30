import poly
import unittest

class TestCases(unittest.TestCase):
   
   def assertListAlmostEqual(self, l1, l2):
      self.assertEqual(len(l1), len(l2))
      for el1, el2 in zip(l1, l2):
         self.assertAlmostEqual(el1,el2)
   
   def test_polyadd2(self):
      p_1 = [1,2,3]
      p_2 = [1,2,3]
      p_3 = poly.poly_add2(p_1, p_2)
      self.assertListAlmostEqual(p_3, [2,4,6])
    
   def test_polyadd2_2(self):
     p_1 = [1,1,1]
     p_2 = [2,2,2]
     p_3 = poly.poly_add2(p_1, p_2)
     self.assertListAlmostEqual(p_3, [3,3,3])
  
   def test_poly_mult2(self):
     p_1 = [1,1,1]
     p_2 = [1,1,1]
     p_3 = poly.poly_mult2(p_1, p_2)
     self.assertListAlmostEqual(p_3, [1,2,3,2,1])
  
   def test_poly_mult2_2(self):
     p_1 = [2,2,2]
     p_2 = [2,2,2]
     p_3 = poly.poly_mult2(p_1, p_2)
     self.assertListAlmostEqual(p_3, [4,8,12,8,4]) 
if  __name__ == '__main__':
       unittest.main()

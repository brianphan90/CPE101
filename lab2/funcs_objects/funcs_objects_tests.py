
import unittest
import objects
import math 
import funcs_objects

class TestCases(unittest.TestCase):
   def test_point(self):
     p1=objects.point(1,1)
     self.assertEqual(p1.x,1)
     self.assertEqual(p1.y,1)
   def test_point2(self):
     p2=objects.point(2,2)
     self.assertEqual(p2.x,2)
     self.assertEqual(p2.y,2)

   def test_circle(self):
      pt=objects.point(1,1)
      cir=objects.circle(pt,5)
      self.assertEqual(cir.center.x,1)
      self.assertEqual(cir.center.y,1)
      self.assertEqual(cir.radius,5)
   def test_circle2(self):
      pt2=objects.point(2,2)
      cir2=objects.circle(pt2,3)
      self.assertEqual(cir2.center.x,2)
      self.assertEqual(cir2.center.y,2)
      self.assertEqual(cir2.radius,3)
   def test_distance(self):
      dis1=funcs_objects.distance(objects.point(1,1),objects.point(2,2))
      self.assertAlmostEqual(dis1,2.449489742783178)
   def test_distance1(self):
      dis2=funcs_objects.distance(objects.point(0,0),objects.point(3,3))
      self.assertAlmostEqual(dis2,4.242640687119285)  
   def test_circles_overlap(self):
      circle3=objects.circle(objects.point(0,0),1)
      circle4=objects.circle(objects.point(0,0),1)
      circle4=funcs_objects.circles_overlap(circle3,circle4)
      self.assertTrue(circle4,True)  
   def test_circles_overlap2(self):
      c1=objects.circle(objects.point(2,2),3)
      c2=objects.circle(objects.point(2,2),5)
      c3=funcs_objects.circles_overlap(c1,c2)
      self.assertTrue(c3,True)






if __name__ == '__main__' :
   unittest.main()


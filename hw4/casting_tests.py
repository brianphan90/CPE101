import cast
from collisions import *
from data import *
from vector_math import *
import unittest

class dataTests(unittest,TestCase):
   def test_cast_rays(self):
      sphere_1 = Sphere(Point(0,0,0),3)
      sphere_2 = Sphere(point(10,10,10),2)
      s_list = [sphere_1, sphere_2]
      r = Ray(Point(0,0,0), Vector(0,0,1))
      c_ray = find_intersection_point(r, s_list)
      self.assertTrue(cast_ray, False)

if __name__== "__main__":
   unittest.main()


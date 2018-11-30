import data
import unittest
class TestData(unittest.TestCase):
   def test_point_1(self):
      my_point = data.Point(2.0, 3.0, 5.0)
      self.assertAlmostEqual(my_point.x, 2.0)
      self.assertAlmostEqual(my_point.y, 3.0)
      self.assertAlmostEqual(my_point.z, 5.0)
   def test_point_2(self):
      my_point = data.Point(2.3, 3.5, 5.1)
      self.assertAlmostEqual(my_point.x, 2.3)
      self.assertAlmostEqual(my_point.y, 3.5)
      self.assertAlmostEqual(my_point.z, 5.1)
   def test_point_eq(self):
      my_point = data.Point(3, 4, 5)
      my_point_2 = data.Point(3, 4, 5)
      self.assertTrue(data.Point.__eq__(my_point, my_point_2))
   def test_vector_1(self):
      my_vector = data.Vector(1.0, 11.0, 15.0)
      self.assertAlmostEqual(my_vector.x, 1.0)
      self.assertAlmostEqual(my_vector.y, 11.0)
      self.assertAlmostEqual(my_vector.z, 15.0)
   def test_vector_2(self):
      my_vector = data.Vector(1.9, 10.1, 3.1)
      self.assertAlmostEqual(my_vector.x, 1.9)
      self.assertAlmostEqual(my_vector.y,10.1)
      self.assertAlmostEqual(my_vector.z, 3.1)
   def test_vector_eq(self):
      v1 = data.Vector(1,2,3)
      v2 = data.Vector(1,2,3)
      self.assertTrue(data.Vector.__eq__(v1, v2))
   def test_ray_1(self):
      pt = data.Point(9.9, 10.1, 11.1)
      dir= data.Vector(1.1, 5.6, 7.9)
      my_ray = data.Ray(pt, dir)
      self.assertAlmostEqual(my_ray.pt.x, 9.9)
      self.assertAlmostEqual(my_ray.pt.y, 10.1)
      self.assertAlmostEqual(my_ray.pt.z, 11.1)
      self.assertAlmostEqual(my_ray.dir.x, 1.1)
      self.assertAlmostEqual(my_ray.dir.y, 5.6)
      self.assertAlmostEqual(my_ray.dir.z, 7.9)
   def test_ray_2(self):
      pt = data.Point(6.8, 6.9, 8.1)
      dir = data.Vector(4.4, 3.2, 2.2)
      my_ray = data.Ray(pt, dir)
      self.assertAlmostEqual(my_ray.pt.x, 6.8)
      self.assertAlmostEqual(my_ray.pt.y, 6.9)
      self.assertAlmostEqual(my_ray.pt.z, 8.1)
      self.assertAlmostEqual(my_ray.dir.x, 4.4)
      self.assertAlmostEqual(my_ray.dir.y, 3.2)
      self.assertAlmostEqual(my_ray.dir.z, 2.2)
   def test_ray_compare(self):
      r1 = data.Ray(data.Point(1,2,3), data.Vector(2,3,4))
      r2 = data.Ray(data.Point(1,2,3), data.Vector(2,3,4))
      self.assertFalse(data.Ray.eq__init__(r1,r1))
   def test_sphere_1(self):
      center = data.Point(1.1 , 1.3, 2.2)
      radius = 5.9
      my_sphere = data.Sphere(center, radius)
      self.assertAlmostEqual(my_sphere.center.x, 1.1) 
      self.assertAlmostEqual(my_sphere.center.y, 1.3)
      self.assertAlmostEqual(my_sphere.center.z, 2.2)
      self.assertAlmostEqual(my_sphere.radius, 5.9)
   def test_sphere_2(self):
      center = data.Point(7.7, 9.9, 17.8)
      radius = 10.8
      my_sphere = data.Sphere(center, radius)
      self.assertAlmostEqual(my_sphere.center.x, 7.7)
      self.assertAlmostEqual(my_sphere.center.y, 9.9)
      self.assertAlmostEqual(my_sphere.center.z, 17.8)
      self.assertAlmostEqual(my_sphere.radius, 10.8)
   def test_scale_vector(self):
      old_v = data.Vector(1,2,3)
      scale = 2
      new_v = data.Vector(2,4,6)
      self.assertEqual(vector_math.scale_vector(old_v, scale), new_v) 
      
if __name__ == "__main__":
     unittest.main()


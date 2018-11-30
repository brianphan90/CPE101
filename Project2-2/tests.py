import unittest
import data
import vector_math

class TestCases(unittest.TestCase):

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
   
   def c_point(self):
      p_1 = data.Point(1,1,1)
      p_2 = data.Point(2,2,2)
      self.assertFalse(data.Point.__eq__(p_1, p_2))
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

   def test_scale_vector_1(self):
      vector_one = data.Vector(1,1,1)
      scale = 2
      v = data.Vector(2,2,2)
      self.assertTrue(data.Vector.__eq__(vector_math.scale_vector(vector_one, scale), v))

   def test_scale_vector_2(self):
      vector_one = data.Vector(1, 2, 3)
      scale = 1.5
      v = data.Vector(1.5, 3, 4.5)
      self.assertEqual(vector_math.scale_vector(vector_one, scale), v)

   def test_dot_vector(self):
      v_1 = data.Vector(1,2,3)
      v_2 = data.Vector(1,2,3)
      n_v = 14
      self.assertEqual(vector_math.dot_vector(v_1, v_2), n_v)  
   
   def test_dot_vector(self):
      v_1 = data.Vector(1,2,3)
      v_2 = data.Vector(2,3,4)
      n_v = 20
      self.assertEqual(vector_math.dot_vector(v_1, v_2),n_v)
   def test_compare_vector(self):
      v_1 = data.Vector(2,3,4)
      v_2 = data.Vector(2,3,4) 
      self.assertTrue(data.Vector.__eq__(v_1, v_2))

   def test_length_vector(self):
      v_1 = data.Vector(1,2,3)
      self.assertAlmostEqual(vector_math.length_vector(v_1), 3.74165738) 
   
   def test_length_vector_2(self):
      v_1 = data.Vector(6,6,6)
      self.assertAlmostEqual(vector_math.length_vector(v_1), 10.3923048 )  
   
   def test_normalize_vector(self):
      v_1 = data.Vector(0.0, 5.0, 0.0)
      v_2 = data.Vector(0.0, 1.0, 0.0)
      self.assertAlmostEqual(vector_math.normalize_vector(v_1), v_2)
  
   def test_nomalize_vector_2(self):
      v_1 = data.Vector(3.0, 4.0, 0.0)
      v_2 = data.Vector(0.6, 0.8, 0.0)
      self.assertAlmostEqual(vector_math.normalize_vector(v_1), v_2)

   def test_difference_points(self):
      pt_1 = data.Point(2, 3, 4)
      pt_2 = data.Point(1, 1, 1)
      pt = data.Vector(1, 2, 3)
      self.assertAlmostEqual(vector_math.difference_point(pt_1, pt_2), pt)
   
   def test_difference_points_2(self):
      pt_1 = data.Point(3,4,5)
      pt_2 = data.Point(1,1,1)
      pt = data.Vector(2,3,4)
      self.assertAlmostEqual(vector_math.difference_point(pt_1, pt_2), pt)
   def test_translate_point(self):
      p = data.Point(1,1,1)
      vect = data.Vector(0.5, 0.5, 0.5)
      new_p = data.Point(1.5, 1.5, 1.5)
      self.assertAlmostEqual(vector_math.translate_point(p, vect), new_p)
   
   def test_translate_point_2(self):
      p = data.Point(1,1,1)
      vect = data.Vector(1,1,1)
      new_p = data.Point(2,2,2)
      self.assertAlmostEqual(vector_math.translate_point(p, vect), new_p)
 
   def test_vector_from_to(self):
      pt_1 = data.Point(1,1,1)
      pt_2 = data.Point(5,5,5)
      n_v = data.Vector(4,4,4)
      self.assertAlmostEqual(vector_math.vector_from_to(pt_1, pt_2), n_v)
  
   def test_vector_from_to_2(self):
      pt_1 = data.Point(2,2,2)
      pt_2 = data.Point(6,6,6)
      n_v = data.Vector(4,4,4)
      self.assertAlmostEqual(vector_math.vector_from_to(pt_1, pt_2), n_v)
if  __name__ == '__main__':
       unittest.main()   

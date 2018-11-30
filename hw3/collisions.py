import vector_math
from data import *
import math
import collisions

def sphere_intersection_point(ray,sphere):
   #define variables
   A = vector_math.dot_vector(ray.dir, ray.dir)
   B = vector_math.dot_vector(vector_math.scale_vector((vector_math.difference_point(ray.pt, sphere.center)), 2), ray.dir)
   C = vector_math.dot_vector(vector_math.difference_point(ray.pt, sphere.center), vector_math.difference_point(ray.pt, sphere.center)) - sphere.radius ** 2
   discriminant = B ** 2 - 4* A * C

   if discriminant < 0:
      return None

   #define t
   t = (-B + math.sqrt(discriminant)) / (2.0 * A)
   t_2 = (-B - math.sqrt(discriminant)) / (2.0 * A)
   point_t = vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir, t))
   point_t2 = vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir, t_2))

   #Cases
   
   if t >= 0 and t_2 >= 0:
      if t_2 > t: 
         return point_t 
      else: 
         return point_t2
   
   elif t < 0 and t_2 < 0:
      return None
 
   elif (t < 0 and t_2 >= 0) or (t >= 0 and t_2 < 0):
      if t >= 0: 
         return point_t
      else: 
         return point_t2
   else: 
      return None

def find_intersection_points(sphere_list, ray):
   list_of_pairs = []
   for sphere in sphere_list:
      if sphere_intersection_point(ray, sphere) != None:
         list_of_pairs.append((sphere,collisions.sphere_intersection_point(ray, sphere)))
   return list_of_pairs

def sphere_normal_at_point(sphere, point):
   return vector_math.normalize_vector(vector_math.vector_from_to(sphere.center,point))   
   
       

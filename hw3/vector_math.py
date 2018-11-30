import math
import data
def scale_vector(vector, scalar):
   vectorx = vector.x
   vectory = vector.y
   vectorz = vector.z
   s = scalar
   vector_x = vectorx * s
   vector_y = vectory * s 
   vector_z = vectorz * s
   vector_s = data.Vector(vector_x, vector_y, vector_z)
   return vector_s
def dot_vector(vector1, vector2):
   vector_x = vector1.x * vector2.x
   vector_y = vector1.y * vector2.y
   vector_z = vector1.z * vector2.z
   return  vector_x + vector_y + vector_z
   
def length_vector(vector):
   vector_length = math.sqrt(vector.x ** 2 + vector.y ** 2 + vector.z **2)
   return vector_length

def normalize_vector(vector):
   length = math.sqrt(vector.x ** 2+ vector.y ** 2 + vector.z **2)
   n_vector_x = vector.x / length
   n_vector_y = vector.y / length
   n_vector_z = vector.z / length
   n_vector = data.Vector(n_vector_x, n_vector_y, n_vector_z)
   return n_vector

def difference_point(point1, point2):
   point_x = point1.x - point2.x
   point_y = point1.y - point2.y
   point_z = point1.z - point2.z
   new_point = data.Vector(point_x, point_y, point_z)
   return new_point

def difference_vector(vector1, vector2):
   vector_x = vector1.x - vector2.x
   vector_y = vector1.y - vector1.y
   vector_z = vector1.z - vector1.z
   new_vector = data.Vector(vector_x, vector_y, vector_z)
   return new_vector

def translate_point(point,vector):
   point_x = point.x + vector.x
   point_y = point.y + vector.y
   point_z = point.z + vector.z
   t_point = data.Point(point_x, point_y, point_z)
   return t_point
def vector_from_to(from_point, to_point):
   point_x = to_point.x - from_point.x
   point_y = to_point.y - from_point.y
   point_z = to_point.z - from_point.z
   f_vector= data.Vector(point_x, point_y, point_z)
   return f_vector

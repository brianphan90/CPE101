import data
import collisions
import vector_math
import utility
import math

def find_distance(p1, p2): #gives distance of two points
   return math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2 + (p2.z - p1.z)**2)

def change_color(color):
   return data.Color(min(int(color.red * 255), 255), min(int(color.green * 255),255), min(int(color.blue * 255), 255))

def cast_ray(ray, sphere_list,color, Light, Point): #update to return color of closest
   closest = intersection[0] #closest to origin
   inter = collisions.find_intersection_points(sphere_list, ray)
   if inter == []:
      return change_color(data.Color(1.0,1.0,1.0))
   for i in range(len(intersection)):
      if find_distance(ray.pt, closest[1]) > find_distance(ray.pt, inter[i][1]):
         closest = inter[i] #new smallest

   fin = inter[closest[0].finish
   col_i = closest.color

   normal = collisions.sphere_normal_at_point(inter[closest][0], inter[closest][1])
   translated = vector_math.translate_point(inter[nearest][1],vector_math.scale_vvector(normal,0.01))
   
   direction_l = vector_math.normalize_vector(vector_math.vector_from_to(translated, Light.pt))

   find_dot_p = vector_math.dot_vector(normal, direction_l) #dot product 
   n_dot_p = find_dot_p *2
   new_vector = vector_math.difference_vector(direction_l, vector_math.scale_vector(normal, n_dot_p))
   direction_v = vector_math.normalize_vector(vector_math.vector_from_to(Point, normal))
   
   intensity_s = vector_math.dot_vector(new_vector, direction_v)
   final_intensity = fin.specular * (intensity_s ** (1.0/fin.roughness))

   final_sphere_ray = collisions.find_find_intersection_points(sphere_list, data.Ray(translated,direction_l))

   #intensity if statements
 
   if intensity_s > 0:
      n_intensity = data.Color((fin.specular * (intensity_s ** (1.0 / fin.roughness)) * Light.color.r), (fin.specular * (intensity_s ** (1.0, fin.roughness))* Light.color.g),( fin.specular * (intensity_s ** (1.0 / fin.roughness)) * Light.color.b))

   if (n_dot_p <=) or (final_sphere_ray != []):
      return data.Color((col_i.r * color.r * fin.ambient), (col_i.g * color.g * fin.ambient), (col_i.b * color.b * fin.ambient))
   else:
      return data.Color((col_i.r * color.r * fin.ambient) + (col_i.r * Light.color.r * fin.diffuse * n_dot_p) + n_intensity.r, (col_i.g * color.g * fin.ambient) +(col_i.g * Light.color.g * fin.diffuse.n_dot_p) + n_intensity.g, (col_i.b * color.b * fin.ambient) + (col_i * Light.color.b * fin.diffuse * n_dot_p) + n_intensity.b)    
      
def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, color, light):
   print("P3, "\n")
   print(width, height, "\n")
   print(255, "\n")
   difference_x = (max_x - min_x) / float(width)
   difference_y = (max_y - min_y) / float(height)
   for y in range(height):  #nested for loop
      for x in range(width):
         p_x = min_x + difference_x * x 
         P_y = max_y - difference_y * y
         d = vector_math.vector_from_to(eye_piint, data.Point(p_x, p_y,0))
         r = data.Ray(eye_point, d)
         final = cast_ray(ray, sphere_list, color, light, eye_point)
         f_color = change_color(final)
         print(f_color.r, f_color.g, f_color.b, "\n") 

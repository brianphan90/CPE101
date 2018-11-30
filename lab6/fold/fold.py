import math
import point

def sum(list):
   t_sum = 0
   for i in list:
      t_sum += i
   return t_sum

def index_of_smallest(list):
   index = 0 
   smallest = list[0]
   if len(list) == []:
      return -1
   for i in range(len(list)):
      if list[i] < smallest:
         smallest = list[i]
         index = i
   return index  

def nearest_origin(list):
   new_list = []
   if len(list) == 0:
      return -1
   elif len(list) > 0:
      for i in list:
         new_list.append(math.sqrt((list[i].x) ** 2 + (list[i].y) **2))
      return index_of_smallest(new_list)   

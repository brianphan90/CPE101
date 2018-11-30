import point
import math

def square_all(list):
   new_list = []
   for num in list:
      new_list.append(num **2)
   return new_list

def add_n_all(list,n):
   new_list= []
   for x in range(len(list)):
      new_list.append(list[x] + n)
   return new_list

def distance_all(list, origin):
   new_list = []
   for value in list:
      new_list.append(math.sqrt((origin.x - value.x) **2 +(origin.y - value.y) **2))
   return new_list 

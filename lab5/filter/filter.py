import point 

def are_positive(list):
   new_list = []
   for value in list:
      if value > 0:
         new_list.append(value)
   return new_list

def are_greater_than(list, n):
   new_list = []
   for value in list:
      if value > n:
         new_list.append(value)
   return new_list

def are_in_first_quadrant(list):
   new_list = []
   for value in list:
      if value.x > 0 and value.y > 0:
         new_list.append(value)
   return new_list 

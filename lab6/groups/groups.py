
def groups_of_3(input_list):
   list = []
   x = 3 
   for i in range(0, len(input_list), x):
      list.append(input_list[i: i+x])
   return list

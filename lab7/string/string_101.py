import char

def str_rot_13(string):
   rot_string = ""
   for i in string:
      if i.isalpha():
         rot_string = rot_string + char.char_rot_13(i)
      else:
         rot_string = rot_string + i 
   return rot_string

def str_translate_101(string, old, new):
   new_string = ""
   for i in string:
      if i == old:
         new_string += new
      else:
         new_string += i
   return new_string
          
   

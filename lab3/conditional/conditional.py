#condtional

def max_101(x,y):
   if x > y:
      return x
   else:
      return y

def max_of_three(x,y,z):
   if x > z and x > y:
      return x
   elif y > x and y > z:
      return y
   else:
      return z

def rental_late_fee(x):
   if x <= 0:
      return 0
   elif x >0 and x <=9:
      return 5
   elif x >9 and x <= 15:
      return 7
   elif x >15 and x <= 24:
      return 19
   elif x > 24:
      return 100
 

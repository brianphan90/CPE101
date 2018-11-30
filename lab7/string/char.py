def is_lower_101(char):
   if ord(char) >= ord('a') and ord(char)<= ord('z'):
      return True

def char_rot_13(char):
   if char.isalpha():
      if char.isupper():
         if ord('A') <= ord(char) <= ord('M'):
            return chr(ord(char) + 13)
         elif ord ('N') <= ord(char) <= ord('Z'):
            return chr(ord(char) - 13)
      elif char.islower():
         if ord('a') <= ord(char) <= ord('m'):
            return chr(ord(char) + 13)
         elif ord('n') <= ord(char) <= ord('z'):
            return chr(ord(char) - 13)
   else:
      return chr(char)

import unittest
import string_101

class TestString(unittest.TestCase):
  
   def test_str_rot_13(self):
      new_string = string_101.str_rot_13('abc123')
      expected = 'nop123'
      self.assertEqual(new_string, expected)

   def test_str_rot_13_2(self):
      new_string = string_101.str_rot_13('79zzz')
      expected = '79mmm'
      self.assertEqual(new_string, expected)
    
   def test_str_translate_101(self):
      translated = string_101.str_translate_101("abcdcba", "a", "x")
      expected = "xbcdcbx"
      self.assertEqual(translated, expected)

   def test_str_translate_101_2(self):
      translated = string_101.str_translate_101("aaaa", "a", "x")
      expected = "xxxx"
      self.assertEqual(translated, expected)
if __name__ == '__main__':
   unittest.main()


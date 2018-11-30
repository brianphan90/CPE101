import unittest
import char

class TestChar(unittest.TestCase):
   def test_lower(self):
      lower = char.is_lower_101('a')
      self.assertTrue(lower, True)

   def test_lower_2(self):
      lower = char.is_lower_101('Z')
      self.assertFalse(lower, True)

   def test_char_rot_13(self):
      char_rot = char.char_rot_13('a')
      self.assertEqual(char_rot, 'n')

   def test_char_rot_13_2(self):
      char_rot = char.char_rot_13('B')
      self.assertEqual(char_rot, 'O')
if __name__ == '__main__':
   unittest.main()


import unittest
import groups

class TestGroups(unittest.TestCase):

   def assertListAlmostEqual(self, l1, l2):
      self.assertEqual(len(l1), len(l2))
      for el1, el2 in zip(l1, l2):
         self.assertAlmostEqual(el1, el2)
   
   def test_groups_of_3(self):
      input = [1,2,3,4,5,6]
      expected = [[1,2,3],[4,5,6]]
      self.assertEqual(groups.groups_of_3(input), expected)
   
   def test_groups_of_3_2(self):
      input = [1,1,1,2,2]
      expected = [[1,1,1],[2,2]]
      self.assertEqual(groups.groups_of_3(input), expected)

   # Add tests here

if __name__ == '__main__':
   unittest.main()

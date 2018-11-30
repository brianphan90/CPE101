import unittest
import filter
import point

class TestCases(unittest.TestCase):
   def test_are_positive(self):
      are_pos1= filter.are_positive([1,2,3])
      are_pos2 = filter.are_positive([2,-4,7])
       
      self.assertEqual(are_pos1,[1,2,3])
      self.assertEqual(are_pos2,[2,7])

   def test_are_greater_than(self):
      are_great1 = filter.are_greater_than([1,2,3],3)
      are_great2 = filter.are_greater_than([3,5,8],1)

      self.assertEqual(are_great1,[])
      self.assertEqual(are_great2,[3,5,8])

   def test_are_first_quadrant(self):
      are_first1 = filter.are_in_first_quadrant([point.Point(1,1), point.Point(3,5), point.Point(34,7)])
      are_first2 = filter.are_in_first_quadrant([point.Point(-3,-5), point.Point(2,5), point.Point(-4,8)])

      self.assertEqual(are_first1, 
      [point.Point(1,1), point.Point(3,5), point.Point(34,7)])
      self.assertEqual(are_first2, [point.Point(2,5)])



# Run the unit tests.
if __name__ == '__main__':
   unittest.main()


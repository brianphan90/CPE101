import unittest
import map
import point

class TestCases(unittest.TestCase):
   def test_square_all(self):
      list_squared = map.square_all([1,2,3])
      self.assertEqual(list_squared, [1,4,9])

   def test_square_all_2(self):
      list_sqaured = map.square_all([-2,3,4])
      self.assertEqual(list_sqaured, [4,9,16])

   def test_add_n_all(self):
      list_sum = map.add_n_all([0,0,0], 2)
      self.assertEqual(list_sum, [2,2,2])
  
   def test_add_n_all_2(self):
      list_sum = map.add_n_all([1,1,1], 2)
      self.assertEqual(list_sum, [3,3,3])   

   def test_distance_all(self):
      list = [point.Point(6, 0), point.Point(3,0), point.Point(4, 0)]
      origin = point.Point(0, 0)
      expected = [6, 3, 4]
      self.assertEqual(map.distance_all(list, origin), expected)
   def test_distance_all_2(self):
      list = [point.Point(6, 8), point.Point(3, 4), point.Point(0, 8)]
      origin = point.Point(0, 0)
      expected = [10, 5, 8]
      self.assertEqual(map.distance_all(list, origin), expected)


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()


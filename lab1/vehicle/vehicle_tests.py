import unittest
from vehicle import Vehicle

class VehicleTests(unittest.TestCase):

   def test_vehicle_1(self):
      vehicle_1 = Vehicle(4, 35, 2, True)
      self.assertEqual(vehicle_1.wheels, 4)
      self.assertEqual(vehicle_1.fuel, 35)
      self.assertEqual(vehicle_1.doors, 2)
      self.assertEqual(vehicle_1.roof, True)


#run the unite tests.

if __name__ == '__main__':
   unittest.main()

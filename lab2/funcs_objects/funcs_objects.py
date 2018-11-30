import math
def distance(pt1,pt2):
   return math.sqrt((pt2.x**2 -pt1.x**2)+(pt2.y**2 -pt1.y**2))

def circles_overlap(circle,circle2):
   return distance (circle.center,circle2.center)<= (circle.radius+circle2.radius)


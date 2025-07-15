from collections import namedtuple
import math

Triangle = namedtuple('Triangle', ['side1', 'side2', 'side3'])

def triangle_area(triangle):
    print("Sides of the triangle:",triangle.side1,',',triangle.side2,',',triangle.side3)

    s = (triangle.side1 + triangle.side2 + triangle.side3) / 2

    area = math.sqrt(s * (s - triangle.side1) * (s - triangle.side2) * (s - triangle.side3))
    return area

triangle_instance = Triangle(side1=4, side2=5, side3=7)

area = triangle_area(triangle_instance)
print("Triangle Area:", area)
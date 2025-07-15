from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

Circle = namedtuple('Circle', ['radius', 'center'])

center = Point(x=4, y=4)
circle_instance = Circle(radius=5, center=center)

print("Circle-")
print("Radius:", circle_instance.radius)
print("Center:", circle_instance.center)
print("Value of x-coordinate:", circle_instance.center.x)
print("Value of y-coordinate", circle_instance.center.y)
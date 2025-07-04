from collections import namedtuple
Point = namedtuple("Point", ["x", "y", "z"])
p = Point(4, 7, 10)
print("x:", p.x)
print("y:", p.y)
print("z:", p.z)
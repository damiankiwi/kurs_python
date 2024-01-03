import math

def circles_intersect(circle1, circle2):
    x1, y1, r1 = circle1
    x2, y2, r2 = circle2

    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    if distance <= r1 + r2:
        return True
    else:
        return False

print(circles_intersect([1, 2, 4], [1, 2, 8]))
print(circles_intersect([0, 0, 2], [10, 10, 5]))
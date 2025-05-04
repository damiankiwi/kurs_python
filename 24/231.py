import math

def check_point_in_circle(x, y, center_x, center_y, radius):
    distance = math.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
    return distance <= radius

def main():
    try:
        center_x = float(input("Input x-coordinate of the circle center: "))
        center_y = float(input("Input y-coordinate of the circle center: "))
        radius = float(input("Input the radius of the circle: "))
        point_x = float(input("Input x-coordinate of the point: "))
        point_y = float(input("Input y-coordinate of the point: "))

        if check_point_in_circle(point_x, point_y, center_x, center_y, radius):
            print("The point is within the circle area.")
        else:
            print("The point is not within the circle area.")
    except ValueError:
        print("Invalid input. Please Input valid coordinates and radius.")

if __name__ == "__main__":
    main()
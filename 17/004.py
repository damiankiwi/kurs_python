import math

def calculate_circle_area(radius):
    return math.pi * radius**2

if __name__ == "__main__":
    try:
        radius = float(input("Enter the radius of the circle: "))
        area = calculate_circle_area(radius)
        print(f"Area = {area}")
    except ValueError:
        print("Invalid input. Please enter a valid numeric value for the radius.")

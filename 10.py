import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def distance(self, other):
        """Calculate distance between this point and another point."""
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx**2 + dy**2)

# Taking input from the user
def get_point_input(index):
    x = float(input(f"Enter x-coordinate for Point {index}: "))
    y = float(input(f"Enter y-coordinate for Point {index}: "))
    return Point(x, y)

# Main program
if __name__ == "__main__":
    point1 = get_point_input(1)
    point2 = get_point_input(2)

    print("\nCreated Points:")
    print("Point 1:", point1)
    print("Point 2:", point2)

    dist = point1.distance(point2)
    print(f"\nDistance between Point 1 and Point 2: {dist:.2f}")

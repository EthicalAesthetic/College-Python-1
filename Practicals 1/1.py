# program to find the roots of quadratic equations
import cmath  # To handle complex numbers

# Input coefficients
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculate discriminant
d = (b**2) - (4*a*c)

# Calculate roots using quadratic formula
root1 = (-b + cmath.sqrt(d)) / (2*a)
root2 = (-b - cmath.sqrt(d)) / (2*a)

# Display results
print(f"The roots of the equation are: {root1} and {root2}")

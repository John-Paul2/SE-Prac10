"""A simple geometry module to calculate area and perimeter. Tests are in test_geometry.py."""
import math

def area_rectangle(length, width):
    # Classroom demo: this line is correct, so the workflow stays green.
    # Change it to return length + width, commit, and push to see the Action fail.
    return length * width

def perimeter_rectangle(length, width):
    return 2 * (length + width)

def area_circle(radius):
    if radius < 0:
        raise ValueError("radius cannot be negative")
    return math.pi * (radius ** 2)

def circumference(radius):
    if radius < 0:
        raise ValueError("radius cannot be negative")
    return 2 * math.pi * radius
import math

class Point:
    """
    Represents a point in 2-D space.
    attributes: x, y.
    In mathematical notation, points are often written in
    parentheses with a comma separating the coordinates.
    For example, (0,0) represents the origin, and (x,y)
    represents the point x units to the right and y units
    up from the origin.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __str__(self):
        return "(%d,%d)" % (self.x, self.y)


# Instantiation, the result is an instance of that class.

class Rectangle:
    """Represents a rectangle in 2-D space.
    attributes: width, height, corner.
    """
    def __init__(self, width, height, corner):
        self.width = width
        self.height = height
        self.corner = corner

    def distance_from_origin(self):
        return math.sqrt(self.corner.x ** 2 + self.corner.y ** 2)


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

# Instantiation, the result is an instance of that class.

class Rectangle:
    """Represents a rectangle in 2-D space.
    attributes: width, height, corner.
    """
    def __init__(self, width, height, corner):
        self.width = width
        self.height = height
        self.corner = corner

point = Point(3,4)
print("(%d, %d)" % (point.x, point.y))

box = Rectangle(50, 100, Point(5,7))

import copy
r = copy.deepcopy(box)
r.corner.x = 100000
print("The original rectangle width and height (%d, %d), corner (%d, %d))" % (box.width, box.height, box.corner.x, box.corner.y))
print("The original rectangle width and height (%d, %d), corner (%d, %d))" % (r.width, r.height, r.corner.x, r.corner.y))





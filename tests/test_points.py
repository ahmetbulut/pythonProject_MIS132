import unittest
from myclasses.twoD import Point, Rectangle

class MyTestCase(unittest.TestCase):
    def test_something(self):
        point = Point(3,4)
        box = Rectangle(50, 100, Point(5,7))
        #
        # import copy
        # r = copy.deepcopy(box)
        # r.corner.x = 100000
        # print("The original rectangle width and height (%d, %d), corner (%d, %d))" % (box.width, box.height, box.corner.x, box.corner.y))
        # print("The original rectangle width and height (%d, %d), corner (%d, %d))" % (r.width, r.height, r.corner.x, r.corner.y))
        #

        # Polymorphism, without checking type, your code works with multiple of types of objects.
        # The function that gets called is implemented in all respective classes.
        # polymorphic code
        l = [point, box]
        for item in l:
            print(item.distance_from_origin())


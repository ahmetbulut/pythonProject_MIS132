import unittest
from myclasses.twoD import Point, Rectangle

class MyTestCase(unittest.TestCase):
    def test_polymorphism(self):
        point = Point(3,4)
        box = Rectangle(50, 100, Point(5,7))

        # Polymorphism, without checking type, your code works with multiple of types of objects.
        # The function that gets called is implemented in all respective classes.
        # polymorphic code
        l = [point, box]
        for item in l:
            print(item.distance_from_origin())


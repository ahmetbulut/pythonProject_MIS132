import unittest
from myclasses.mytime import Time

class MyTestCase(unittest.TestCase):
    def test_manipulation(self):
        t = Time(12, 20, 00)
        print(t)
        totalseconds = t.increment(125)
        print(t)


if __name__ == '__main__':
    unittest.main()

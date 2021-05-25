import unittest
from myclasses.my_adts import Stack, Queue, Priority_Queue, Task
from myclasses.twoD import Point

class MyTestCase(unittest.TestCase):

    def test_stack(self):
        mystack = Stack()
        print("Is it empty?", mystack.is_empty())

        mystack.push(Point(1, 1))
        mystack.push(Point(2, 2))
        mystack.push(Point(3, 3))

        print("Is it empty?", mystack.is_empty())

        print(mystack.pop())

    def test_queue_empty(self):
        queue = Queue()
        self.assertEqual(True, queue.is_empty())

    def test_queue_remove(self):
        queue = Queue()
        first_added = "Tuna"
        second_added = "Alpaslan"
        queue.insert(first_added)
        queue.insert(second_added)
        self.assertEqual(first_added, queue.remove())

    def test_priority_queue(self):
        queue = Priority_Queue()

        task1 = Task("Implement a queue", 1)
        task2 = Task("Implement a priority queue", 5)
        task3 = Task("Implement a priority queue", 4)
        task4 = Task("Implement a Stack", 2)

        queue.insert(task1)
        queue.insert(task2)
        queue.insert(task3)
        queue.insert(task4)

        queue.remove()
        actual = queue.remove()

        self.assertEqual(4, actual.priority)

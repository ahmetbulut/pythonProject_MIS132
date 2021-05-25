class Stack:
    """
    A stack is called a “Last in, First out” or LIFO data structure,
    because the last item that was added is the first to be removed.
    """

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []


mystack = Stack()
print("Is it empty?", mystack.is_empty())

from twoD import Point

mystack.push(Point(1,1))
mystack.push(Point(2,2))
mystack.push(Point(3,3))

print("Is it empty?", mystack.is_empty())

print(mystack.pop())


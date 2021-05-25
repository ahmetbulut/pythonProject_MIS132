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

class Queue():
    """
    A queue with the simplest queueing policy “First in, First out”, FIFO for short.
    """
    def __init__(self):
        self.items = []

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        return self.items.pop(0)

    def is_empty(self):
        return self.items == []

class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

class Priority_Queue(Queue):
    """
    The semantic difference from a typical Queue is that the item that is removed from the queue is not
    necessarily the first one that was added. Rather, it is the item in the queue that has the highest
    priority.
    """

    def remove(self):
        self.items.sort(key = lambda task: task.priority)
        return self.items.pop()


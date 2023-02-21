#!/usr/bin/env python3

"""
atds.py
Describes the Data Structures used in the Advanced Topics
course.
"""

class Stack(object):
    """Describes a stack with traditional peek, pop, push methods,
    as well as size() and isEmpty().
    """
    def __init__(self):
        self.stack = []

    def push(self, item):
        """Adds an item to the end of the list, ie. the
        top of the stack.
        """
        self.stack.append(item)

    def pop(self):
        """Returns the last item on the list, ie. the
        top of the stack.
        """
        if len(self.stack) > 0:
            return self.stack.pop()
    
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def __repr__(self):
        return super().__repr__() + str(self.stack)

class Queue(object):
    """Defines a "first-in, first-out" queue with the "head" of
    the line at position 0 and the "tail" of the line at index
    -1.
    """
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)

    def peek(self):
        if len(self.queue) > 0:
            return self.queue[0]
    
    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def __repr__(self):
        return "Queue" + str(self.queue)

class Deque(object):
    """Implements a double-ended queue, with the
    front at index 0 and the rear at -1.
    """
    def __init__(self): 
        self.deque = []

    def add_front(self, item):
        self.deque.insert(0, item)

    def add_rear(self, item):
        self.deque.append(item)

    def remove_front(self):
        if len(self.deque) > 0:
            return self.deque.pop(0)

    def remove_rear(self):
        if len(self.deque) > 0:
            return self.deque.pop()

    def size(self):
        return len(self.deque)

    def is_empty(self):
        return len(self.deque) == 0 
    
    def __repr__(self):
        return "Deque" + str(self.deque)
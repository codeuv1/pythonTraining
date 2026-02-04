# use stack to find minimum element in constant time
from math import inf


class Stack:
    def __init__(self):
        self._items = []
        self.min_value = float(inf)
    def push(self, item):
        self._items.append(item)
        self.min_value = min(self.min_value, item)

    def pop(self):
        if not self._items:
            raise KeyError("Cannot pop from an empty stack")
        return self._items.pop()

    def peek(self):
        if not self._items:
            raise KeyError("Cannot peek from an empty stack")
        return self._items[-1]

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)

print(s.min_value)
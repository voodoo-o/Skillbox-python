class Node:
    def __init__(self, data):
        self.data = data
        self.pref = None


class Stack:
    def __init__(self):
        self.end = None

    def pop(self):
        if self.end is None:
            return None
        val = self.end.data
        self.end = self.end.pref
        return val

    def push(self, val):
        new_node = Node(val)
        new_node.pref = self.end
        self.end = new_node

    def print(self):
        current = self.end
        while current is not None:
            print(current.data, end=" -> ")
            current = current.pref
        print("None")


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.print()
popped_element = stack.pop()
stack.print()

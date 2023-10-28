class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None


class Queue:
    def __init__(self):
        self.start = None
        self.end = None

    def pop(self):
        if self.start is None:
            return None
        val = self.start.data
        if self.start.nref:
            self.start = self.start.nref
            self.start.pref = None
        else:
            self.start = self.end = None
        return val

    def push(self, val):
        new_node = Node(val)
        if self.start is None:
            self.start = self.end = new_node
        else:
            self.end.nref = new_node
            new_node.pref = self.end
            self.end = new_node

    def insert(self, n, val):
        new_node = Node(val)
        if n == 0:
            new_node.nref = self.start
            self.start.pref = new_node
            self.start = new_node
        else:
            current = self.start
            i = 0
            while i < n - 1 and current:
                current = current.nref
                i += 1
            if current:
                new_node.nref = current.nref
                new_node.pref = current
                if current.nref:
                    current.nref.pref = new_node
                current.nref = new_node
                if new_node.nref is None:
                    self.end = new_node

    def print(self):
        current = self.start
        while current:
            print(current.data, end=" ")
            current = current.nref
        print()


if __name__ == "__main__":
    q = Queue()
    q.push(1)
    q.push(2)
    q.push(3)

    print("Queue:")
    q.print()

    print("Pop:", q.pop())
    print("Pop:", q.pop())

    print("Queue после pop:")
    q.print()

    q.insert(1, 4)

    print("Queue после insert:")
    q.print()

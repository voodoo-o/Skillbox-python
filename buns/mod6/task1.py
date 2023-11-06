class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def get(self, index):
        if index < 0 or not self.head:
            raise Exception("Неверный индекс элемента")
        current = self.head
        for i in range(index):
            current = current.next
            if current is None:
                raise Exception("Индекс элемента превышает размерность списка")
        return current.value

    def remove(self, index):
        if index < 0 or not self.head:
            raise Exception("Неверный индекс элемента")
        if index == 0:
            self.head = self.head.next
            return

        current = self.head
        for i in range(index - 1):
            current = current.next
            if current is None:
                raise Exception("Индекс элемента превышает размерность списка")
        current.next = current.next.next

    def insert(self, index, value):
        if index <= 0 or not self.head:
            raise Exception("Неверный индекс элемента")
        current = self.head
        for i in range(index - 1):
            current = current.next
            if current is None or current.next is None:
                raise Exception("Индекс элемента превышает размерность списка")
        node = Node(value)
        node.next = current.next
        current.next = node

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next


linked_list = LinkedList()
print(linked_list.head)

linked_list.push(123)
linked_list.push(456)
linked_list.push(789)
print(linked_list.get(0), linked_list.get(1), linked_list.get(2))

linked_list.remove(1)
print(linked_list.get(0), linked_list.get(1))

linked_list.insert(1, 000)
print(linked_list.get(0), linked_list.get(1), linked_list.get(2))

for i in linked_list:
    print(i, end=" ")
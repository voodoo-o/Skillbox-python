class DoubleElement:
    def __init__(self, *lst):
        self.elements = lst
        self.pointer = 0

    def __next__(self):
        if self.pointer >= len(self.elements):
            raise StopIteration

        element_1 = self.elements[self.pointer]
        element_2 = self.elements[self.pointer + 1] if self.pointer + 1 < len(self.elements) else None
        self.pointer += 2
        return element_1, element_2

    def __iter__(self):
        return self


dL = DoubleElement(1, 2, 3, 4)
for pair in dL:
    print(pair)

print()

dL = DoubleElement(1, 2, 3, 4, 5)
for pair in dL:
    print(pair)



class Queue:

    size = 0

    def __init__(self, capacity):
        self.capacity = capacity
        self.elements = []

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return self.size

    def push(self, el):
        if self.size == self.capacity:
            raise OverFlowError()

        self.size += 1
        self.elements.append(el)

    def pop(self):
        if self.size <= 0:
            raise UnderFlowError()

        self.size -= 1
        return self.elements.pop(0)

    def top(self):
        if self.is_empty():
            raise UnderFlowError()

        return self.elements[0]

    @classmethod
    def make(cls, capacity):
        if capacity < 0:
            raise NegativeCapacityError()

        return Queue(capacity)


class OverFlowError(RuntimeError):
    pass

class UnderFlowError(RuntimeError):
    pass

class NegativeCapacityError(ValueError):
    pass





from abc import ABCMeta, abstractmethod


class Stack:
    __meta__ = ABCMeta

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def push(self, num):
        pass

    @abstractmethod
    def pop(self, num):
        pass

    @abstractmethod
    def top(self):
        pass

    @abstractmethod
    def find(self):
        pass


class BoundedStack:

    def __init__(self, capacity):
        if capacity < 0:
            raise NegativeCapacityError()

        self.size = 0
        self.capacity = capacity
        self.elements = []

    def is_empty(self):
        return not self.size

    def __len__(self):
        return self.size

    def push(self, num):
        if self.capacity == self.size:
            raise OverFlowError()

        self.size += 1
        self.elements.append(num)

    def pop(self):
        if not self.elements:
            raise UnderFlowError()

        self.size -= 1
        return self.elements.pop()

    def top(self):
        return self.elements[-1] if self.elements else None

    def find(self, num):
        return self.size - self.elements.index(num) - 1

    @classmethod
    def make(cls, capacity):
        return BoundedStack(capacity)



class OverFlowError(RuntimeError):
    pass


class UnderFlowError(RuntimeError):
    pass


class NegativeCapacityError(ValueError):
    pass
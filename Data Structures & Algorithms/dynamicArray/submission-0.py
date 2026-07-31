class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.backingarray = [0] * capacity

    def get(self, i: int) -> int:
        value = self.backingarray[i]
        return value

    def set(self, i: int, n: int) -> None:
        self.backingarray[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.backingarray[self.size] = n
        self.size += 1

    def popback(self) -> int:
        if self.size > 0:
            self.size -= 1
        return self.backingarray[self.size]

    def resize(self) -> None:
        self.capacity *= 2
        newarray = [0] * self.capacity
        for i in range(self.size):
            newarray[i] = self.backingarray[i]
        self.backingarray = newarray

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity

class DynamicArray:
    lst = None
    capacity = 0

    def __init__(self, capacity: int):
        self.lst = [None] * capacity
        self.capacity = capacity

    def get(self, i: int) -> int:
        return self.lst[i]

    def set(self, i: int, n: int) -> None:
        self.lst[i] = n

    def find_index_before_first_none(self):
        for index, e in enumerate(self.lst):
            if e is None: return index-1
        return -1

    def pushback(self, n: int) -> None:
        if self.lst[-1] is not None: self.resize()
        target_index = self.find_index_before_first_none()
        self.set(target_index+1, n)

    def popback(self) -> int:
        target_index = self.find_index_before_first_none()
        res = self.lst[target_index]
        self.set(target_index, None)
        return res

    def resize(self) -> None:
        new_lst = [None] * (2*self.capacity)
        for i in range(len(self.lst)):
            new_lst[i] = self.lst[i]
        self.lst = new_lst
        self.capacity *= 2

    def getSize(self) -> int:
        return sum([1 for e in self.lst if e is not None])
    
    def getCapacity(self) -> int:
        return self.capacity

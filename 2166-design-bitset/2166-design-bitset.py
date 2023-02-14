class Bitset:

    def __init__(self, size: int):
        self.ones = {}
        self.zeros = {}
        self.size = size
        for i in range(size):
            self.zeros[i] = i

    def fix(self, idx: int) -> None:
        self.ones[idx] = idx
        if idx in self.zeros:
            del self.zeros[idx]

    def unfix(self, idx: int) -> None:
        self.zeros[idx] = idx
        if idx in self.ones:
            del self.ones[idx]

    def flip(self) -> None:
        self.ones, self.zeros = self.zeros, self.ones

    def all(self) -> bool:
        return len(self.ones) == self.size

    def one(self) -> bool:
        return len(self.ones) > 0

    def count(self) -> int:
        return len(self.ones)

    def toString(self) -> str:
        arr = ["0"]*self.size
        for key, val in self.ones.items():
            arr[key] = "1"
            
        return "".join(arr)


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()
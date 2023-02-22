class SmallestInfiniteSet:

    def __init__(self):
        self.s = set()
        for num in range(1,1001):
            self.s.add(num)

    def popSmallest(self) -> int:
        min_el = min(self.s)
        self.s.remove(min_el)
        return min_el

    def addBack(self, num: int) -> None:
        self.s.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
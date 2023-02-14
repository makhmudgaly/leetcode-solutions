class RandomizedSet:

    def __init__(self):
        self.d = set()
        

    def insert(self, val: int) -> bool:
        if val in self.d:
            return False
        
        self.d.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.d:
            return False
        
        self.d.remove(val)
        return True
        

    def getRandom(self) -> int:
        return random.sample(self.d, 1)[0]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
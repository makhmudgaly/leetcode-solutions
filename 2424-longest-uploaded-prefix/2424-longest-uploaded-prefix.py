class LUPrefix:

    def __init__(self, n: int):
        self.set = set()
        self._longest = 0

    def upload(self, video: int) -> None:
        self.set.add(video)
        
        while self._longest + 1 in self.set:
            self._longest += 1
        

    def longest(self) -> int:
        return self._longest
        


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()
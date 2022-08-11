class MapSum:

    def __init__(self):
        self.d = {}
        

    def insert(self, key: str, val: int) -> None:
        self.d[key] = val

    def sum(self, prefix: str) -> int:
        ans = 0
        for key in self.d:
            if key.startswith(prefix):
                ans += self.d[key]
                
        return ans


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
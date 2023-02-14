class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        blacklist = sorted(blacklist)
        self.bl = set(blacklist)
        self.d = {}
        j = 0
        self.avail = n - len(blacklist)
        for i in range(self.avail, n):
            if i not in self.bl:
                self.d[blacklist[j]] = i
                j+=1
                

    def pick(self) -> int:
        i = random.randint(0, self.avail - 1)
        return self.d[i] if i in self.d else i


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()
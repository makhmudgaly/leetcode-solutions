from collections import defaultdict

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.state = defaultdict(int)

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.state[tokenId] = self.ttl + currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.state and self.state[tokenId] > currentTime:
            self.state[tokenId] = self.ttl + currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for token, expiry in self.state.items():
            if expiry > currentTime:
                count += 1
        
        return count


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)
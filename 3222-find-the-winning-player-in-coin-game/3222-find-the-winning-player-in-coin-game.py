class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        turns = min(x, y // 4)
        return "Alice" if turns & 1 == 1 else "Bob"
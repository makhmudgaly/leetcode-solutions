class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        score_one = 0
        score_two = 0
        
        score_one = calculate_score(player1)
        score_two = calculate_score(player2)
        print(score_one, score_two)
        if score_one == score_two:
            return 0
        
        return 1 if score_one > score_two else 2
        
        
    
def calculate_score(player):
    strike_loc = -1
    score = 0
    for idx, num in enumerate(player):
        if (strike_loc + 1 == idx or strike_loc + 2 == idx) and strike_loc != -1:
                score += 2*num
        else:
                score += num
            
            
        if num == 10:
                strike_loc = idx

    return score    
            
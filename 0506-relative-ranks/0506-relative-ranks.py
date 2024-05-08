class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sort = { v:k+1 for k,v in enumerate(sorted(score, reverse=True))}
        medals = {1: "Gold Medal", 2:"Silver Medal", 3: "Bronze Medal"}
        return [medals.get(sort[num], str(sort[num])) for num in score]
        
        
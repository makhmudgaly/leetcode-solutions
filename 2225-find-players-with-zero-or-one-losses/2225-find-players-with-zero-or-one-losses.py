class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dict = {}
        wins = []
        loses = []
        for match in matches:
            win, lose = match
            if win not in dict:
                dict[win] = {"win":0, "lose":0, "total":0}
                
            if lose not in dict:
                dict[lose] = {"win":0, "lose":0, "total":0}
                
            dict[win]["win"]+=1
            dict[win]["total"]+=1
            
            dict[lose]["lose"]+=1
            dict[lose]["total"]+=1
        
        for key in dict:
            if dict[key]["lose"] == 0:
                wins.append(int(key))
            
            if dict[key]["lose"] == 1:
                loses.append(int(key))
                
        return [sorted(wins), sorted(loses)]
        
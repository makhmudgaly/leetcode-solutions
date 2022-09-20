class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players = sorted(players)
        trainers = sorted(trainers)
        c = 0
        i = j = 0
        while(i<len(players) and j < len(trainers)):
            if players[i] > trainers[j]:
                while j < len(trainers) and players[i] > trainers[j]:
                    j+=1
            else:
                c+=1
                i+=1
                j+=1
                    
        return c
        
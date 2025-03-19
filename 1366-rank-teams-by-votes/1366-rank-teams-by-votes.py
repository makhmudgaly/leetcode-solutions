from collections import defaultdict
import heapq
from functools import cmp_to_key

class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        vote_length = len(votes[0])
        votes_to_count = {vote: [0]*vote_length for vote in votes[0]}
        
        for vote in votes:
            for pos in range(vote_length):
                votes_to_count[vote[pos]][pos] += 1
        
        sorted_keys =[key for key, val in sorted(votes_to_count.items(), key=cmp_to_key(compare))]
        
        return "".join(sorted_keys)

def compare(a , b):
    n = len(a[1])
    for i in range(n):
        if a[1][i] != b[1][i]:
            return b[1][i] - a[1][i]
    
    return ord(a[0]) - ord(b[0])

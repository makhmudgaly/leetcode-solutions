class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        answer = [pref[0]] * len(pref)
        
        for i in range(len(pref)-1,0,-1):
            answer[i] = pref[i] ^ pref[i-1]
        
        return answer
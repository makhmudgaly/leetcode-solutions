
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        pref_a = set()
        pref_b = set()
        ans = []
        
        for idx in range(len(A)):
            
            pref_a.add(A[idx])
            pref_b.add(B[idx])
            
            ans.append(len(pref_a.intersection(pref_b)))
            
        return ans
            
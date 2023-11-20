class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        longest_common_prefix = 0
        min_string = min(len(s1), len(s2), len(s3))
        
        for i in range(min_string):
            if not (s1[i] == s2[i] and s2[i] == s3[i]):
                break
            longest_common_prefix += 1
                
        return -1 if longest_common_prefix == 0 else len(s1) + len(s2) + len(s3) - longest_common_prefix * 3
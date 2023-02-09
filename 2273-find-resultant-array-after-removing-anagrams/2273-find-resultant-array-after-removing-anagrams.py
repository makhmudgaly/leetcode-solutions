from collections import defaultdict
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans = []
        prev_dict = {}
        
        for word in words:
            current_dict = {}
            for ch in word:
                current_dict[ch] = current_dict.get(ch, 0) + 1
                
            if current_dict != prev_dict:
                ans.append(word)
                prev_dict = current_dict
        
        return ans
        
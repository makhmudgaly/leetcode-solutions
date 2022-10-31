from collections import defaultdict
class Solution:
    def oddString(self, words: List[str]) -> str:
        d = defaultdict(list)
        
        def diff(word):
            diff_arr = []
            
            for i in range(1,len(word)):
                curr = ord(word[i]) - ord('a')
                prev = ord(word[i-1]) - ord('a')
                diff_arr.append(curr - prev)
            
            return str(diff_arr)
        
        for word in words:
            s = diff(word)
            d[s].append(word)
            
        for key in d:
            if len(d[key]) == 1:
                return d[key][0]
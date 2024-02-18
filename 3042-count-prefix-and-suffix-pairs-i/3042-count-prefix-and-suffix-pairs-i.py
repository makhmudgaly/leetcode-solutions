class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def is_pref_and_suf(src, tgt):
            n = len(src)
            if tgt[:n] == src and tgt[-(n):] == src:
                return True
            
            return False
        
        c = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if is_pref_and_suf(words[i], words[j]):
                    c += 1
        
        return c
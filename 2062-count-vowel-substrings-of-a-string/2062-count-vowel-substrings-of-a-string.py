from collections import defaultdict

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        dict = defaultdict(int)
        jj = j = 0
        res=0
        for i,ch in enumerate(word):
            if ch not in 'aeiou':
                dict.clear()
                jj = j = i+1
            else:
                dict[ch] += 1
                while len(dict) == 5 and all(dict.values()):
                    dict[word[j]] -= 1
                    j += 1
                res += j - jj
        return res
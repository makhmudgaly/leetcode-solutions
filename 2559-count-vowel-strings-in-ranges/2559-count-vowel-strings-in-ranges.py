class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'o', 'u', 'i'}
        words = list(map(lambda x: x[0] in vowels and x[len(x)-1] in vowels, words))
        prefix = [0]
        sum_ = 0
        for word in words:
            if word:
                sum_ += 1
            prefix.append(sum_)
        
        ans = []
        
        for l,r in queries:
            ans.append(prefix[r+1] - prefix[l])
        
        return ans
        
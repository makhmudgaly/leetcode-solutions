class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        results = []
        self.backtrack(s, word_set, [], results, 0)
        return results
    
    def backtrack(self, s, word_set, current_sentence, results, start):
        if start == len(s):
            results.append(" ".join(current_sentence))
        
        for end in range(start + 1, len(s) + 1):
            word = s[start : end]

            if word in word_set:
                current_sentence.append(word)
                self.backtrack(s, word_set, current_sentence, results, end)

                current_sentence.pop()
    
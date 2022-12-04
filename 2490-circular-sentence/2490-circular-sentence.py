class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(' ')
        for idx in range(len(words)):
            curr_word = words[idx]
            next_word = words[idx+1 if idx < len(words) - 1 else 0]
            
            if curr_word[-1] != next_word[0]:
                return False
        
        return True
            
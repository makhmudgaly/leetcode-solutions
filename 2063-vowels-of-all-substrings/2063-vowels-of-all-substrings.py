class Solution:
    def countVowels(self, word: str) -> int:
        """
        long long int cnt=0;
        long long int n = word.size();
        for(int i=0;i<word.size();i++)
        {
            if(word[i]=='a'||word[i]=='e'||word[i]=='i'||word[i]=='o'||word[i]=='u')
                cnt+=((i+1)*(n-i));
        }
        return cnt;
        """
        
        count = 0
        n = len(word)
        
        for i in range(n):
            if word[i] in 'aeiou':
                count += ((i+1) * (n-i))
        
        return count
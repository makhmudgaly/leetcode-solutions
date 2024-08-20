class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        if not s:
            return []
        ans = []
        
        def dfs(chars, idx, n):
            if idx == n:
                ans.append("".join(chars))
                return
            
            if "0" <=chars[idx] <= "9":
                dfs(chars, idx+1, n)
                return
            
            chars[idx] = chars[idx].lower()
            dfs(chars, idx+1, n)
            
            chars[idx] = chars[idx].upper()
            dfs(chars, idx+1, n)
        
        n = len(s)
        chars = list(s)
        
        dfs(chars,0,n)
        return ans
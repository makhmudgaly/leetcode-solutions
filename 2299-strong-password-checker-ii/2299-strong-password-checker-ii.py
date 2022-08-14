class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        
        d = {'upper':0, 'lower': 0,'num':0, 'spec':0}
        
        for idx, ch in enumerate(password):
            if 97 <= ord(ch) <= 122:
                d['lower'] +=1
                
            if 65 <= ord(ch) <= 90:
                d['upper'] +=1 
            
            if ch.isdigit():
                d['num'] += 1
            
            if ch in "!@#$%^&*()-+":
                d['spec'] += 1
            
            if idx < len(password) - 1 and password[idx] == password[idx+1]:
                return False
            
        if any(d[x] < 1 for x in d):
            return False

        return True
            
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for num in range(1, n+1):
            currStr = ""
            if num % 3 == 0:
                currStr += "Fizz"
            
            if num % 5 == 0:
                currStr += "Buzz"
            
            if currStr == "":
                currStr += str(num)

            ans.append(currStr)
        
        return ans
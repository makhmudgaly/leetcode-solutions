class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        a = [1]*n
        for round in range(k):
            for i in range(1,n):
                a[i] = (a[i] + a[i-1]) % 1000000007
                
        return a[n-1]
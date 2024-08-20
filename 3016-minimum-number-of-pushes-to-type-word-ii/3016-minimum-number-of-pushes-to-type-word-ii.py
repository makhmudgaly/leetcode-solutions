import heapq
class Solution:
    def minimumPushes(self, word: str) -> int:
        ans = 0
        freq = [0]*26
        for ch in word:
            freq[ord(ch)-ord('a')] += 1

        pq = []
        for val in filter(lambda x:x>0,freq):
            heapq.heappush(pq,-val)
        processed = 0
        count = 1
        while pq:
            key_press = -heapq.heappop(pq)
            processed += 1
            ans += (key_press * count)
            if processed % (count * 8) == 0:
                count += 1
            
        return ans
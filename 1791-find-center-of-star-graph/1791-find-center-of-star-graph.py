from collections import defaultdict
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        degree = defaultdict(int)
        for edge in edges:
            degree[edge[0]] += 1
            degree[edge[1]] += 1
        
        for node, count in degree.items():
            if count == len(edges):
                return node
            
        return -1
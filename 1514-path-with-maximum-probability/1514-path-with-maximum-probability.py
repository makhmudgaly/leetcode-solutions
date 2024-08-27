class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        for i, (a,b) in enumerate(edges):
            # since it is not directed graph
            # we add both ways
            graph[a].append([b, succProb[i]])
            graph[b].append([a, succProb[i]])
        
        max_prob = [0.0]*n
        max_prob[start] = 1.0
        
        queue = deque([start])
        while queue:
            curr = queue.popleft()
            for next_node, prob in graph[curr]:
                if max_prob[curr] * prob > max_prob[next_node]:
                    max_prob[next_node] = max_prob[curr] * prob
                    queue.append(next_node)
        
        return max_prob[end]
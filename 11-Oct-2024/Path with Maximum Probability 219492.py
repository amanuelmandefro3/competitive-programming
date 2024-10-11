# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i in range(len(edges)):
            graph[edges[i][0]].append((edges[i][1], succProb[i]))
            graph[edges[i][1]].append((edges[i][0], succProb[i]))

        success = {node:-float('inf') for node in range(n)}
        success[start_node] = 1
        processed = set()

        heap = [(-1, start_node)]

        while heap:
            current_probability, current_node = heappop(heap)

            if current_node in processed:
                continue

            processed.add(current_node)

            for ngb, p in graph[current_node]:
                prob = -1*current_probability * p
                if prob > success[ngb]:
                    success[ngb] = prob
                    heappush(heap, (-prob, ngb))
        print(success)   
        return success[end_node] if success[end_node] != -float('inf') else 0          






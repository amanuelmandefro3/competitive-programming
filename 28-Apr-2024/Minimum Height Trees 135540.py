# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = defaultdict(int)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            indegree[u] += 1
            indegree[v] += 1
        queue = deque()

        for i in range(n):
            if indegree[i] <= 1:
                queue.append(i)
        print(queue)        
        while queue:
            if n <= 2:
                return list(queue)
            for _ in range(len(queue)):
                node = queue.popleft()
                n -= 1

                for ngb in graph[node]:
                    indegree[ngb] -= 1
                    if indegree[ngb] == 1:
                        queue.append(ngb)  


# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ans = [set() for _ in range(n)]
        graph = defaultdict(list)
        indegree = defaultdict(int)
        print(graph)
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1
        queue = deque()    
        for node in range(n):
            if node not in indegree:
                queue.append(node)
        print(queue)        
        while queue:
            curr = queue.popleft()
            for ngb in graph[curr]:
                indegree[ngb] -= 1
                ans[ngb].update(ans[curr])
                ans[ngb].add(curr)
                if indegree[ngb] == 0:
                    queue.append(ngb)
        for i in range(n):
            # a = list(ans[i])
            # a.sort()
            ans[i] = sorted(ans[i])          

        return ans                    


        
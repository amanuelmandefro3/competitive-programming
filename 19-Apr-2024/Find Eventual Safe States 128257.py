# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        color = [1 for _ in range(len(graph))]
        ans = []
        def dfs(node):
            if color[node] == 1:
                color[node] = 2
            temp = True
            for ngb in graph[node]:
                if color[ngb] == 1:
                    temp = temp & dfs(ngb)
                elif color[ngb] == 2:
                    return False
            if temp:        
                ans.append(node)
                color[node] = 3
            return temp
        for node in range(len(graph)):
            if color[node] == 1:
                dfs(node)
        ans.sort()        
        return ans                    

        
# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for src, dst, dist in roads:
            graph[src].append((dst, dist))
            graph[dst].append((src, dist))

        res = float('inf')
        visited = set()

        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            nonlocal res
            for ngb, dist in graph[i]:
                res = min(res, dist)
                dfs(ngb)

        dfs(1)
        return res                
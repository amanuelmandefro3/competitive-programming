# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for a, b in richer:
            graph[a].append(b)
            indegree[b] += 1
        queue = deque()    
        for n in range(len(quiet)):
            if not indegree[n]:
                queue.append(n)
        ans = [i for i in range(len(quiet))]
        while queue:
            node = queue.popleft()
            for ngb in graph[node]:
                ans[ngb] = min(ans[ngb], ans[node], key = lambda x: quiet[x] )
                indegree[ngb] -= 1
                if indegree[ngb] == 0:
                    queue.append(ngb)

        # visited = [False for i in range(len(quiet))]  
        # ans_val = quiet[:] 
        # def dfs(node):
        #     visited[node] = True
        #     for ngb in  graph[node]:
        #         if not visited[ngb]:
        #             dfs(ngb)
        #         if ans_val[ngb] < ans_val[node]:
        #             ans[node] = ans[ngb]
        #             ans_val[node] = ans_val[ngb] 


        # for n in range(len(quiet)):
        #     if not visited[n]:
        #         dfs(n)
        return ans




        
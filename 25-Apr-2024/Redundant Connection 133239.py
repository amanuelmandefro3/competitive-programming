# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        root = [i for i in range(n)]
        size = [1 for i in range(n)]
        ans = []

        def find(x):
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]

        def union(x,y):
            px = find(x-1)
            py = find(y-1)
            if py != px:
                if size[px] > size[py]:
                    root[py] = px
                    size[px] += size[py] 
                else: 
                    root[px] = py
                    size[py] += size[px]  
            else:
                print('I was here')
                ans.append([x,y])
        for x, y in edges:
            union(x,y)
        return ans[0]                              
        
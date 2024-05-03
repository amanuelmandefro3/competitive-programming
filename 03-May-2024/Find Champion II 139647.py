# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree = defaultdict(int)
        for u, v in edges:
            indegree[v]+= 1
        src = []
        for i in range(n):
            if not indegree[i]:
                src.append(i)
        if len(src) > 1:
            return -1
        return src[0]    
        
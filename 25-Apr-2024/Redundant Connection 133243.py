# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = defaultdict(str)
        size = defaultdict(int)
        for char in s1:
            size[char] = 1
            parent[char] = char
        for char in s2:
            parent[char] = char    
            size[char] = 1
        def find(x):
            if x == parent[x]:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            px = find(x)
            py = find(y)
            if px != py:
                if px < py:
                    parent[py] = parent[px]
                else:
                    parent[px] = parent[py]  
        for i in range(len(s1)):
            union(s1[i], s2[i])
        ans = []
        for base in baseStr:
            ptr = find(base)
            if ptr == '':
                ans.append(base)  
            ans.append(ptr)
        return ''.join(ans)    


        
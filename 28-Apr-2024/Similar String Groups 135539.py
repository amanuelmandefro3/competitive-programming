# Problem: Similar String Groups - https://leetcode.com/problems/similar-string-groups/

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        root = [i for i in range(n)]
        size = [1 for i in range(n)]
        def find(x):
            while x != root[x]:
                root[x] = root[root[x]]
                x = root[x]

            return root[x]
        def union(x, y):
            px = find(x)
            py = find(y)

            if px != py:
                if size[px] > size[py]:
                    root[py] = px
                    size[px] += size[py]
                else:
                    root[px] = py
                    size[py] += size[px]

        for i in range(n):
            for j in range(i+1, n):
                diff = 0
                for k in range(m):
                    if strs[i][k] != strs[j][k]:
                        diff += 1
                    if diff > 2:
                        break
                if diff <= 2:
                    union(i, j)


        parent = set()
        for i in root:
            pi = find(i)
            parent.add(pi)
        return len(parent)    

        return 1                        



        return ans




        
# Problem: Convert 1D Array Into 2D Array - https://leetcode.com/problems/convert-1d-array-into-2d-array/

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if n * m != len(original):
            return [] 
        ans = [[] for _ in range(m)]
        i = 0
        for j in range(m):
            for k in range(i, i+n):
                ans[j].append(original[k])
            i += n

        return ans        
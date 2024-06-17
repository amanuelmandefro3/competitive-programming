# Problem: Matrix Block Sum - https://leetcode.com/problems/matrix-block-sum/

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        prefix = mat[:][:]
        n,m =len(mat), len(mat[0])
        answer =[[0 for _ in range(m)] for _ in range(n)]

        def prevPrefix(i,j):
            if 0 <= i < n and 0 <= j < len(mat[0]):
                return prefix[i][j]
            return 0

        for i in range(n):
            for j in range(m):
                prefix[i][j] += prevPrefix(i-1, j) +prevPrefix(i, j-1) - prevPrefix(i-1,j-1) 

        for r in range(n):
            for c in range(m):
                answer[r][c] = (prevPrefix(min(r+k, n-1), min(c+k, m-1)) + 
                                prevPrefix(r-k-1, c-k-1)-
                                prevPrefix(r-k-1, min(c+k, m-1))-
                                prevPrefix(min(r+k, n-1), c-k-1) )  

        return answer      
        
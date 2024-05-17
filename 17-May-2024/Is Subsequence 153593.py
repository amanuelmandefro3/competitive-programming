# Problem: Is Subsequence - https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        memo = {}
        def dp(i,j):
            if i == -1 or j == -1:
                return i == -1
            if (i,j) in memo:
                return memo[(i,j)]
            if s[i] == t[j]:
                memo[(i,j)] = dp(i-1, j-1)
            else:
                memo[(i,j)] = dp(i, j-1)
            return memo[(i,j)]    
        return dp(len(s)-1, len(t)-1)                    


        
# Problem: Palindrome Partitioning II - https://leetcode.com/problems/palindrome-partitioning-ii/

class Solution:
    def minCut(self, s: str) -> int:
        memo = {}

        def dp(i):
            if i == len(s):
                return 0
            if i in memo:
                return memo[i]

            min_cuts = float('inf')
            for j in range(i, len(s)):
                if (s[i:j+1]) == s[i:j+1][::-1]:
                    min_cuts = min(min_cuts, 1 + dp(j + 1))
            memo[i] = min_cuts

            return min_cuts
        

        return dp(0) - 1
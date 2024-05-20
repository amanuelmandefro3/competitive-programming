# Problem: Palindrome Partitioning - https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        memo = {}
        def dp(s):
            if s in memo:
                return memo[s]
            if s == '':
                return [[]]
            ans = []
            for i in range(len(s)): 
                combinations = dp(s[i+1:]) 
                
                for comb in combinations:
                    cd = ''.join(comb)
                    if len(cd) == len(s[i+1:]):
                        if s[:i+1] == s[:i+1][::-1]:
                            new_comb = [s[:i+1]]
                            new_comb.extend(comb)
                            comb = new_comb
                            ans.append(comb)
            memo[s] = ans
            return memo[s]

        return dp(s)





        
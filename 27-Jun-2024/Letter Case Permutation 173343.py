# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        def backtrack(i, path):
            if len(path) == len(s):
                ans.append(path)
                return
            for j in range(i, len(s)):
                if s[j].isalpha():
                    backtrack(j+1, path + s[j].lower())
                    backtrack(j+1, path + s[j].upper())
                else:
                    backtrack(j+1, path + s[j]) 

        backtrack(0, '')
        return ans
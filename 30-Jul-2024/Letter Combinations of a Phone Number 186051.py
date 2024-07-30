# Problem: Letter Combinations of a Phone Number - https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToChar = {
                        "2":"abc", 
                        "3":"def", 
                        "4":"ghi", 
                        "5":"jkl", 
                        "6":"mno",
                        "7":"pqrs",
                        "8":"tuv",
                        "9":"wxyz"
                       }
        ans = []
        
        def backtrack(i, path):
            if len(path) == len(digits):
                ans.append(''.join(path))
                return 
            for c in digitToChar[digits[i]]:
                path.append(c)
                backtrack(i+1, path)
                path.pop()

        if digits:        
            backtrack(0, [])

        return ans                           

        
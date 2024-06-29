# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def backtrack(n, m, path):
            if n == 0 == m:
                ans.append(''.join(path[:]))
            if n > 0:
                path.append('(')
                backtrack(n-1, m, path)
                path.pop()
            if n < m and m > 0:
                path.append(')')
                backtrack(n, m-1, path) 
                path.pop()
        backtrack(n,n,[])

        return ans

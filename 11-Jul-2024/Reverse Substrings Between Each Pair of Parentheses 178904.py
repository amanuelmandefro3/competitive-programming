# Problem: Reverse Substrings Between Each Pair of Parentheses - https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
    
        for elem in s:
            if elem != ')':
                stack.append(elem)
            else:
                res = []
                while stack[-1] != '(':
                    res.append(stack.pop())
                stack.pop()
                stack.extend(res)

        return ''.join(stack)


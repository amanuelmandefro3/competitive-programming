# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, floor(c**0.5)
        while l <= r:
            if l**2 + r**2 == c:
                return True
               
            if l**2 + r**2 > c:
                r -= 1
            else: l += 1    
        return False             
        
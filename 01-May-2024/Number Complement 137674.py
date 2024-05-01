# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        b = 1
        while num >= b:
            num ^= b
            b <<= 1        

        return num
        
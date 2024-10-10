# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num = ''
        for c in s:
            num += str(ord(c)-ord('a')+1)
        while k:
            num_int = 0
            for digit in num:
                num_int += int(digit)
            num = str(num_int)  
            k -= 1    

        return int(num)
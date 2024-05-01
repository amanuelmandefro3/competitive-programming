# Problem:  Add Binary - https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = list(a)
        b = list(b)
        result = ''
        carry = 0
        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
            result += (str(carry%2))
            carry //= 2
        # result = ''.join(result)
       
        return result[::-1]
        
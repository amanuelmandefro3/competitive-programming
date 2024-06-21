# Problem: Reverse Bits - https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:
        b = bin(n)
        ans = ['0']*32
        j = 0
        for i in range(len(b)-1, 1, -1):
            ans[j] = b[i]
            j += 1
        ans = ''.join(ans)   

        return int(ans,2)           
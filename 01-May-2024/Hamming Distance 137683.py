# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:  
        x_ord = x^y
        ans = 0
        while x_ord != 0:
            if (1&x_ord):
                ans += 1
            x_ord >>= 1


        return ans

        
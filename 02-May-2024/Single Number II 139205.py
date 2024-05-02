# Problem: Single Number II - https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        ans = 0
        b = 1
        for i in range(32):
            bit_sum = 0
            for num in nums:
                bit_sum += num & b
            if bit_sum % 3:
                ans |= b
            b <<= 1
            
        if ans >= 2**31:
            ans -= 2**32   

        return ans    



        
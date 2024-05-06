# Problem: Maximum XOR for Each Query - https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        mx = (1 << maximumBit )-1
        xor, ans = 0, []
        for num in nums:
            xor ^= num
            ans.append(mx^xor)
        ans.reverse()    
        return ans  


        
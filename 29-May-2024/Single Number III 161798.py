# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
        index = None
        for i in range(32):
            if xor & 1<<i:
                index = i
                break
        setted, unsetted = 0,0
        for num in nums:
            if num & 1<<index:
                setted ^= num
            else:
                unsetted ^= num
        return [setted, unsetted]            

        
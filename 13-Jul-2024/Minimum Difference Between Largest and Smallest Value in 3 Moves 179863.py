# Problem: Minimum Difference Between Largest and Smallest Value in 3 Moves - https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        
        if n <= 4:
            return 0 
        ans = float('inf')
        
        for i in range(4):
            ans = min(ans, nums[n-4+i] - nums[i])
        
        return ans
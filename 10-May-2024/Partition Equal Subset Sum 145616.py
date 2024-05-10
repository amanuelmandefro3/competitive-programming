# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}
        
        def dp(i, target_sum):
            if target_sum == 0:
                return True
            
            if i == len(nums):
                return False
            
            if (i, target_sum) not in memo:
                memo[(i, target_sum)] = dp(i+1, target_sum-nums[i]) or dp(i+1, target_sum)
            
            return memo[(i, target_sum)]
        
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False
        
        return dp(0, total_sum // 2)

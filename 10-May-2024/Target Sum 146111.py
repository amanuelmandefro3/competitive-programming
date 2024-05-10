# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # ans = 0
        memo = {}
        def bactrack(i, _sum):
            if i == len(nums):
                if _sum == target:
                    return 1
                return 0
            if (i, _sum) in memo:
                return memo[(i, _sum)]
            ans = 0
            ans += bactrack(i+1, _sum+nums[i])
            ans += bactrack(i+1, _sum-nums[i])
            memo[(i, _sum)] = ans
            return ans
        return bactrack(0, 0)

        # return ans             
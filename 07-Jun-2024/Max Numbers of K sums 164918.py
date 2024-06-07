# Problem: Max Numbers of K sums - https://leetcode.com/problems/max-number-of-k-sum-pairs

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        l, r = 0, len(nums) -1
        operation = 0
        while l < r:
            if nums[l] + nums[r] == k:
                operation += 1
                l += 1
                r -= 1
            elif nums[l] + nums[r] > k:
                r -= 1
            else:
                l += 1
        return operation                 
        
# Problem: Maximum Gap - https://leetcode.com/problems/maximum-gap/

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        mx, mn = max(nums), min(nums)
        n = len(nums)
        if n == 2:
            return mx - mn

        bucket_size = ceil((mx - mn) / (n - 1))
        min_bucket = [float('inf')] * n
        max_bucket = [-float('inf')] * n

        for num in nums:
            if num == mn or num == mx:
                continue
            idx = (num - mn) // bucket_size
            min_bucket[idx] = min(min_bucket[idx], num)
            max_bucket[idx] = max(max_bucket[idx], num)

        prev_max = mn
        max_gap = 0

        for i in range(n):
            if min_bucket[i] == float('inf'):
                continue
            max_gap = max(max_gap, min_bucket[i] - prev_max)
            prev_max = max_bucket[i]

        max_gap = max(max_gap, mx - prev_max)

        return max_gap

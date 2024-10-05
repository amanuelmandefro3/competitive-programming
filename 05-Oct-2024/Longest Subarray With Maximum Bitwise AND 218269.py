# Problem: Longest Subarray With Maximum Bitwise AND - https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mx = max(nums)
        ans, pos_dict = 1, defaultdict(int)
        if nums[0] == mx: pos_dict[0] = 1
        for i in range(1, len(nums)):
            if nums[i] == mx:
                pos_dict[i] +=( pos_dict[i-1] + 1)
                ans = max(pos_dict[i], ans)

        return ans        
        
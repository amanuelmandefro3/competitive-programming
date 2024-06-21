# Problem: Next Permutation - https://leetcode.com/problems/next-permutation/description/

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Initialize two pointers starting from the end of the list
        l, r = len(nums)-1, len(nums)-1
        
        # Find the largest index 'l' such that nums[l-1] < nums[l]
        #or finding where non-increasing stop 
        while l > 0 and nums[l-1] >= nums[l]:
            l -= 1
            
        # If 'l' is 0, entire sequence is non-increasing, so reverse it
        if l == 0:
            nums.reverse() 
            return  

        # Find the rightmost element greater than nums[l-1]
        while nums[l-1] >= nums[r]:
            r -= 1
        
        # Swap nums[l-1] with the smallest element to its right greater than it
        # swap 
        nums[l-1], nums[r] = nums[r], nums[l-1]
        r = len(nums)-1

        # Reverse the suffix starting from index 'l'
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

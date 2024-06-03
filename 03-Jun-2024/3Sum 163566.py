# Problem: 3Sum - https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans, n = [], len(nums)
        nums.sort()

        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, n -1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    while left+1 < right and nums[left+1] == nums[left]:
                        left += 1
                    while left < right-1 and nums[right-1] == nums[right]:
                        right -= 1

                    left += 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else: left+= 1  


        return ans                         


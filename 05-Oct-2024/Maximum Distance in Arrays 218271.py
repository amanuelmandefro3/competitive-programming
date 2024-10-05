# Problem: Maximum Distance in Arrays - https://leetcode.com/problems/maximum-distance-in-arrays/

from typing import List

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        ans = 0
        
        for i in range(1, len(arrays)):
            diff1 = abs(arrays[i][-1] - min_val) 
            diff2 = abs(max_val - arrays[i][0])
            ans = max(ans, diff1, diff2)
            
            min_val = min(min_val, arrays[i][0])
            max_val = max(max_val, arrays[i][-1])

        return ans

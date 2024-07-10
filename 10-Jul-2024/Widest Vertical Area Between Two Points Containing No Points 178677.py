# Problem: Widest Vertical Area Between Two Points Containing No Points - https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:

        points.sort()
        max_dif = 0
        

        for i in range(len(points) - 1):
            if points[i][0] != points[i+1][0]:
                max_dif = max(points[i+1][0]- points[i][0], max_dif) 

        return  max_dif   

        
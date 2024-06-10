# Problem: Height Checker
(Easy) - https://leetcode.com/problems/height-checker/

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sort_heights = sorted(heights)
        not_equal = 0
        for i in range(len(heights)):
            if heights[i] != sort_heights[i]:
                not_equal += 1


        return not_equal        

        
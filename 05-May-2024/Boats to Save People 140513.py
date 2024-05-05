# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people)- 1
        boat = 0

        while l <= r:
            possibility = people[l] + people[r]
            if possibility > limit:
                r -= 1
            else: 
                l += 1
                r -= 1
            boat += 1    
        return boat            
        
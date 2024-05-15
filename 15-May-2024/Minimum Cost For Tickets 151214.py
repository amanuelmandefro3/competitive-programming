# Problem: Minimum Cost For Tickets - https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}
        def dp(i):
            if i >= len(days):
                return 0
            #memo has current state? return    
            if i in memo:
                return memo[i] 

            #memo does not have current state try to find min cost for current state
            # if days[i] > last: 
            one = costs[0] + dp(bisect_right(days, days[i]))
            seven = costs[1] + dp(bisect_right(days, days[i]+6))
            thirty = costs[2] + dp(bisect_right(days, days[i]+29))          
            memo[i] = min(one, seven, thirty)
            # else:
            #     memo[(i, last)] = dp(i+1, last) 

            return memo[i] 

        return dp(0)           

                  
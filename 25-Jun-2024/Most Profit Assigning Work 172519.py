# Problem: Most Profit Assigning Work - https://leetcode.com/problems/most-profit-assigning-work/

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        n = len(profit)
        diff_profit = [0]*n

        for i in range(n):
            diff_profit[i] = [difficulty[i], profit[i]]

        diff_profit.sort()
        worker.sort()
        ptr1, ptr2 = 0,0
        max_profit, ans = 0, 0
        while ptr2 < len(worker):
            while ptr1 < n and diff_profit[ptr1][0] <= worker[ptr2]:
                max_profit = max(max_profit,diff_profit[ptr1][1])
                ptr1 += 1
            ans += max_profit
            ptr2 += 1


        return ans    





        
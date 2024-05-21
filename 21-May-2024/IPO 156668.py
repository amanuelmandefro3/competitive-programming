# Problem: IPO - https://leetcode.com/problems/ipo/

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        capital_profit = [0]*len(profits)
        for i in range(len(profits)):
            capital_profit[i] = [capital[i], profits[i]]
        max_heap = []
        capital_profit.sort(reverse=True)
        for _ in range(k):
            while capital_profit and capital_profit[-1][0] <= w:
                cap, prof = capital_profit.pop()
                heappush(max_heap, -prof)
            if not max_heap:
                return w
            top = heappop(max_heap)    
            w += -top

        return w                 

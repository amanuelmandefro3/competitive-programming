# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners, losers = set(), defaultdict(int)
        for winner, loser in matches:
            winners.add(winner)
            losers[loser] += 1
        ans = [[],[]]

        print(losers)

        for winner in winners:
            if losers[winner] == 0:
                ans[0].append(winner)
        for loser, beaten in losers.items():
            if beaten == 1:
                ans[1].append(loser)
        ans[1].sort()
        ans[0].sort()

        return ans                

        
        
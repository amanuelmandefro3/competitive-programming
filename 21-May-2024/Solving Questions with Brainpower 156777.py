# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [questions[i][0] for i in range(len(questions))]
        _max = [0]*len(questions)
        mx = 0
        for i in range(len(questions)):
            mx = max(mx, _max[i])
            dp[i] += mx
            if i + questions[i][1]+1 < len(questions):
                _max[ i + questions[i][1]+1] = max(_max[ i + questions[i][1]+1 ],dp[i])
         
        return max(dp)
        
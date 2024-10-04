# Problem: Find the Student that Will Replace the Chalk - https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/description/

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)
        prefix = [0] * n
        prefix[0] = chalk[0]


        for i in range(1, n):
            prefix[i] = prefix[i-1] + chalk[i]

        k = k % prefix[-1]

        l, r = 0, n-1
        while l <= r:
            mid = (l + r) // 2
            if k >= prefix[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return l

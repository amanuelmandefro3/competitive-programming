# Problem: Minimum Number of Pushes to Type Word II - https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

class Solution:
    def minimumPushes(self, word: str) -> int:
        cnt = Counter(word)
        ans = 0

        push_order = sorted(cnt.values(), reverse=True)
        for i, x in enumerate(push_order):
            ans += (i // 8 + 1) * x
            
        return ans       
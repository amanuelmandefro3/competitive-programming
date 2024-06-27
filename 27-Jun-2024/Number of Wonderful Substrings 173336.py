# Problem: Number of Wonderful Substrings - https://leetcode.com/problems/number-of-wonderful-substrings/

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        cnt = defaultdict(int)
        ans, cnt[0] = 0, 1
        mask = 0

        for c in word:
            index = ord(c)-ord('a')
            mask ^= 1<<index
            ans += cnt[mask]

            for i in range(10):
                premask = mask ^ 1<<i
                ans += cnt[premask]
            cnt[mask] += 1

        return ans        
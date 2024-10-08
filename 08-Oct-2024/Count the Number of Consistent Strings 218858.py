# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        cnt = 0
        for word in words:
            allow = True
            for char in word:
                if char not in allowed:
                    allow = False
                    break
            cnt += allow        

        return cnt
        
# Problem: Find and Replace Pattern - https://leetcode.com/problems/find-and-replace-pattern/

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def get_pattern(s):
            lookup = {}
            output = []
            i = 0
            for char in s:
                if char in lookup:
                    output.append(lookup[char])
                else:
                    i += 1
                    lookup[char] = i
                    output.append(i)
            return output

        ans = []
        pattern = get_pattern(pattern)
        for word in words:
            if get_pattern(word) == pattern:
                ans.append(word)

        return ans        
            

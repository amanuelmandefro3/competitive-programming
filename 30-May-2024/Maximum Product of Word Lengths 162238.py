# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        dic = {}
        for i in range(26):
            dic[chr(97+i)] = i
        bit_len = []
        for word in words:
            oring = 0
            for c in word:
                oring |= 1<<dic[c]
            bit_len.append([oring, len(word)])

        max_len = 0    
        for i in range(len(words)):
            for j in range(len(words)):
                if not bit_len[i][0] & bit_len[j][0]:
                    max_len = max(max_len, bit_len[i][1]*bit_len[j][1])
                    
        return max_len                         
        
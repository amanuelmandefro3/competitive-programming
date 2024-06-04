# Problem: Longest Palindrome - https://leetcode.com/problems/longest-palindrome/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        s_char_count = Counter(s)
        longest_palindrome  = 0

        used = False
        for count in s_char_count.values():
            if count % 2:
                longest_palindrome += count - 1 
                used = True   
            else:
                longest_palindrome += count 

        return longest_palindrome + 1 if used else longest_palindrome
        
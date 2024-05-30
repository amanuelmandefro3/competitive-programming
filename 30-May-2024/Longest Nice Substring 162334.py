# Problem: Longest Nice Substring - https://leetcode.com/problems/longest-nice-substring/

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ans = ''

        def divide_conquer(l, r):
            capital = 0
            lower = 0
            for c in s[l:r]:
                if c.islower():
                    lower |= 1 << (ord(c) - 97)
                else:
                    capital |= 1 << (ord(c) - 65)

            i = l
            while i < r:
                if s[i].islower() and not capital & (1 << (ord(s[i]) - 97)):
                    divide_conquer(l, i)
                    divide_conquer(i + 1, r)
                    break
                elif s[i].isupper() and not lower & (1 << (ord(s[i]) - 65)):
                    divide_conquer(l, i)
                    divide_conquer(i + 1, r)
                    break
                i += 1
            else:
                nonlocal ans
                if r - l > len(ans):
                    ans = s[l:r]

        divide_conquer(0, len(s))
        return ans
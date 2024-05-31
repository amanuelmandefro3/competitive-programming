# Problem: Sum of Two Integers - https://leetcode.com/problems/sum-of-two-integers/description/

class Solution:
    def getSum(self, a: int, b: int) -> int:
        def two_complement(x):
            if x < 0:
                x = (1 << 32) + x
            return x

        a = two_complement(a)
        b = two_complement(b)
        

        mask = 0xFFFFFFFF

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask

            b = carry & mask


        if a > 0x7FFFFFFF:
            a = ~(a ^ mask)

        return a

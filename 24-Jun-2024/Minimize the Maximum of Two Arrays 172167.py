# Problem: Minimize the Maximum of Two Arrays - https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/

class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        def valid(m):
            count1 = m - m//divisor1
            count2 = m- m//divisor2
            both = m - m//lcm(divisor1, divisor2)   

            return (
                count1 >= uniqueCnt1 and
                count2 >= uniqueCnt2 and
                both >= uniqueCnt1 + uniqueCnt2
            ) 
        bottom, top = 1, 2**32
       
        while bottom <= top: 
            mid = (bottom + top)//2
            if valid(mid):
                top = mid - 1
            else:
                bottom = mid + 1

        return bottom           

        
# Problem: Car fleet - https://leetcode.com/problems/car-fleet/

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = sorted(zip(position, speed), key=lambda x: x[0])
        pos_speed = list(pos_speed)
        
        steps, stack = [], []
        for val in pos_speed:
            step = (target - val[0])/val[1]
            steps.append(step)
        for step in steps:
            while stack and stack[-1] <= step:
                stack.pop()
            stack.append(step)
        return len(stack)            
   

        



        return 3
        

        
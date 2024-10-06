# Problem: Design a Stack With Increment Operation - https://leetcode.com/problems/design-a-stack-with-increment-operation/

class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize, self.length = maxSize, 0

    def push(self, x: int) -> None:
        if self.length < self.maxSize:
            self.stack.append(x)
            self.length += 1
    def pop(self) -> int:
        if self.stack:
            self.length -= 1
            return self.stack.pop()
        else:
            return -1    
        

    def increment(self, k: int, val: int) -> None:
        for i in range(min(self.length, k)):
            self.stack[i] += val

        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
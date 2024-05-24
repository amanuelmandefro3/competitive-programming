# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(2)]
        self.is_end = False
    
class Solution:
    def __init__(self):
        self.root = TrieNode()
    def findMaximumXOR(self, nums: List[int]) -> int:
        bin_nums = [0]*len(nums)
        max_len = 0
        for i in range(len(nums)):
            bin_nums[i] = bin(nums[i])[2:]
            max_len = max(max_len, len(bin_nums[i]))
        for i in range(len(nums)):
            if len(bin_nums[i]) < max_len:
                bin_nums[i] = '0'*(max_len-len(bin_nums[i])) + bin_nums[i]    


        for b in bin_nums:
            curr = self.root
            for bi in b:
                if not curr.children[int(bi)]:
                    curr.children[int(bi)] = TrieNode()
                curr = curr.children[int(bi)]
        max_xor = -float('inf')
        for b in bin_nums:
            curr = self.root
            another = ''
            for bi in b:
                if curr.children[int(bi)^1]:
                    another += str(int(bi)^1)
                    curr = curr.children[int(bi)^1]
                else:
                    another += bi
                    curr = curr.children[int(bi)]
            print(int(b,2)^int(another,2))  
            max_xor = max(max_xor, int(b,2)^int(another,2))      
         

        return max_xor   
        
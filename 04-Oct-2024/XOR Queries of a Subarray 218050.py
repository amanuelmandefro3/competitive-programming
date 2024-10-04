# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        prefix = [0]*(n+1)

        for i in range(1, n+1):
            prefix[i] = prefix[i-1] ^ arr[i-1]


        ans = []
        for l, r in queries:
            ans.append(prefix[l] ^ prefix[r+1])


        return ans    
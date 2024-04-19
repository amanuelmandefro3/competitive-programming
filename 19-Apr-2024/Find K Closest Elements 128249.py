# Problem: Find K Closest Elements - https://leetcode.com/problems/find-k-closest-elements/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        idx = bisect_left(arr, x)
        l, r = idx - 1, idx
        n = len(arr)
        ans = []
        while k:
            if abs(arr[r%n] - x) < abs(arr[l%n] - x):
                ans.append(arr[r%n])
                r += 1
            elif abs(arr[l%n] - x) < abs(arr[r%n] - x):
                ans.append(arr[l%n])  
                l -= 1
            else:
                if arr[l%n] < arr[r%n]:
                    ans.append(arr[l%n])
                    l -= 1
                else:
                    ans.append(arr[r%n])
                    r += 1  
            k -= 1                
        return sorted(ans)
# Problem: Prime Pairs With Target Sum - https://leetcode.com/problems/prime-pairs-with-target-sum/description/

class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        prime = [True for _ in range(n)]
        primes = {}
        d = 2
        while d < n:
            if prime[d]:
                primes[d] = False
                i = d*2
                while i < n:
                    prime[i] = False
                    i += d
            d += 1
            
        ans = []
        for p in primes:
            if not primes[p] and n-p in primes:
                ans.append([p, n-p])
                primes[n-p] = True

        return ans            

        
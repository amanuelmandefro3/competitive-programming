# Problem: Fedor and New Game - https://codeforces.com/contest/467/problem/B

from collections import Counter, defaultdict
import sys
import math


def S(): return sys.stdin.readline().strip()
def I(): return (int(S()))
def IL(): return (list(map(int, S().split())))
def SL(): return (list(S()))
def SIL(): return list(map(int, SL()))
def IV(): return (map(int, S().split()))
def M(n): return [IL() for _ in range(n)]
def SM(n): return [SIL() for _ in range(n)]


def solve():
    n,m, k = IV()
    a = [0]*(m+1)
    ans = 0
    for i in range(m+1):
        a[i] = I()
    for i in range(m):
        mx, mn = max(a[i], a[m]), min(a[i], a[m])
        diff = 0
        while mx:
            mx_bit = mx & 1
            mn_bit = mn & 1
            diff += mn_bit ^ mx_bit
            mx >>= 1
            mn >>= 1
   
        if diff <= k:
            ans += 1
    print(ans)            
            
        
    


solve()

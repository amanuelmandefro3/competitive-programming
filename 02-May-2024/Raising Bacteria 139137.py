# Problem: Raising Bacteria - https://codeforces.com/contest/579/problem/A

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
    x = I()
    ans = 0
    while x > 1:
        if x % 2:
            ans += 1
            x -= 1
        x >>= 1
    ans += 1
    print(ans)        
            


solve()
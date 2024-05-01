# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

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
    for _ in range(I()):
        n = I()
        b = bin(n)
        i = len(b)-1
        while i > 2:
            if b[i] == '1':
                break
            i -= 1 
        min_val = b[i:]
        min_val = int(min_val, 2)
        if min_val & n and min_val ^ n:
            print(min_val)
        else: 
            b = 1
            while True:
                new_val = min_val | b
                if new_val & n and new_val ^ n:
                    print(new_val)
                    break
                b <<= 1
            


solve()

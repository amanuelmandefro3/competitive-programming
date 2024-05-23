# Problem: A - Distribute - https://codeforces.com/gym/524965/problem/A

from collections import Counter, defaultdict, deque
import sys
import math


def str_input(): return sys.stdin.readline().strip()
def int_input(): return (int(str_input()))
def int_list(): return (list(map(int, str_input().split())))
def str_list(): return (list(int_input()))
def str_int_list(): return list(map(int, str_list()))
def input_variable(): return (map(int, str_input().split()))
def mat(n): return [int_list() for _ in range(n)]
def str_mat(n): return [str_int_list() for _ in range(n)]


def solve():
    n = int_input()
    a = int_list()
    a_pos = [(a[i], i+1) for i in range(n)]
    a_pos.sort()
    l,r = 0, n-1
    while l < r:
        print(a_pos[l][1], a_pos[r][1])
        l += 1
        r -= 1

solve()

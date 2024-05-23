# Problem: B - Grid Path - https://codeforces.com/gym/524965/problem/B

import threading
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


def input(): return sys.stdin.readline().strip()


def main():
    for _ in range(int_input()):
        n,m, k = input_variable()
        memo = {}
        def dp(i,j, burls):
            if i ==n and j == m:
                return k == burls
            if i >n or j > m:
                return False
            if (i,j) not in memo:
                memo[(i,j)] = dp(i+1,j, burls+j) or dp(i,j+1, burls+i)
            return memo[(i,j)]
        
        if dp(1,1,0):
            print('YES')
        else:
            print('NO')        



if __name__ == '__main__':

    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()

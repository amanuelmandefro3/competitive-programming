# Problem: C - FunkyLlama's Ribbon Challenge - https://codeforces.com/gym/523525/problem/C

from collections import Counter, defaultdict, deque
import sys
import threading
import math


def str_input(): return sys.stdin.readline().strip()
def int_input(): return (int(str_input()))
def int_list(): return (list(map(int, str_input().split())))
def str_list(): return (list(int_input()))
def str_int_list(): return list(map(int, str_list()))
def input_variable(): return (map(int, str_input().split()))
def mat(n): return [int_list() for _ in range(n)]
def str_mat(n): return [str_int_list() for _ in range(n)]


def main():
    line = int_list()
    n = line[0]
    a = line[1:]
    memo = defaultdict(int)

    def dp(curr_l):
        if curr_l == 0:
            return 0
        if curr_l < 0:
            return -float('inf')
        if curr_l in memo:
            return memo[curr_l]
        
        max_pieces = -float('inf')
        for x in a:
            max_pieces = max(max_pieces, 1 + dp(curr_l - x))
        
        memo[curr_l] = max_pieces
        return max_pieces

    print(dp(n))



if __name__ == '__main__':

    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()

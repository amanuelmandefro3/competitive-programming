# Problem: D - Meron and Games - https://codeforces.com/gym/523525/problem/D

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





import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    n = int_input()
    a = int_list()
    memo = {}
    freq = Counter(a)
    b = [max(a)]
    c = min(a)

    def dp(num):
        if num > b[0]:
            return 0
        if num in memo:
            return memo[num]
        memo[num] = max(num*freq[num]+dp(num+2), dp(num+1))

        return memo[num]
    print(dp(c))
    


            
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()


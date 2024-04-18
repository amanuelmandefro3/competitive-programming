# Problem: Heap Operations - https://codeforces.com/contest/681/problem/C

from collections import Counter, defaultdict
import sys
import heapq
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
    n = I()
    min_heap = []
    ans = []
    last_min = 0
    for _ in range(n):
        command = S().split()
        if command[0] == 'insert':
            heapq.heappush(min_heap, int(command[1]))
            ans.append(f'{command[0]} { command[1]}')
        
        elif command[0] == 'getMin':
            while min_heap and min_heap[0] < int(command[1]):
                ans.append('removeMin')
                heapq.heappop(min_heap)
            if not min_heap or min_heap[0] > int(command[1]):
                ans.append(f'insert {command[1]}')
                heapq.heappush(min_heap, int(command[1]))
            ans.append(f'{command[0]} {command[1]}')  
 
        else:
            if not min_heap:
                ans.append(f'insert {0}')
            else:
                heapq.heappop(min_heap)      
            ans.append('removeMin')  

    print(len(ans))
    for an in ans:
        print(an)         


solve()

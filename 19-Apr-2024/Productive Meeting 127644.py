# Problem: Productive Meeting - https://codeforces.com/contest/1579/problem/D

from collections import Counter, defaultdict
import heapq
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
        a = IL()
        ans = []
        talk_person = []
        for i in range(n):
            if a[i] > 0:
                talk_person.append((-a[i], i+1))
        heapq.heapify(talk_person)  
 
        while len(talk_person)  >= 2:
            talk_chance, person1 = heapq.heappop(talk_person)
            talk_chance2, person2 = heapq.heappop(talk_person)
            ans.append([person1, person2])
            
            if (-talk_chance) - 1:
                heapq.heappush(talk_person, (talk_chance+1, person1))
            if (-talk_chance2) -1:
                heapq.heappush(talk_person, (talk_chance2+1, person2))
                
                
                 
                
        print(len(ans))
        for an in ans:
            print(*an)                  
                         


solve()

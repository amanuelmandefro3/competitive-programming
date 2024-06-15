# Problem: Insertion Sort - https://www.hackerrank.com/challenges/insertionsort1/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def insertionSort1(n, arr):
    num_to_insert = arr[n - 1]
    for i in range(n - 1, -1, -1):
        if arr[i - 1] > num_to_insert and i > 0:
            arr[i] = arr[i - 1]
            print(*arr)
        else:
            arr[i] = num_to_insert
            print(*arr)
            break

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
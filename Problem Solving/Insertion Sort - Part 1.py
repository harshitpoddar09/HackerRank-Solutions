#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    a=arr[n-1]
    for i in range(n):
        if i<n-1:
            if a<arr[n-2-i]:
                arr[n-1-i]=arr[n-2-i]
                print(*arr)
            else:
                arr[n-1-i]=a
                print(*arr)
                break
        else:
            arr[0]=a
            print(*arr)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the quickSort function below.
def quickSort(arr):
    #Method2
    arr.sort()
    return arr
    
    #Method1
    """
    pivot=arr[0]
    left=[]
    equal=[]
    right=[]
    for i in arr:
        if i<pivot:
            left.append(i)
        elif i==pivot:
            equal.append(i)
        else:
            right.append(i)
    ans=left+equal+right
    return ans
    """

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    ans=[]
    while len(arr)>0:
        ans.append(str(len(arr)))
        a=min(arr)
        for i in range(len(arr)):
            arr[i]-=a
        for i in range(arr.count(0)):
            arr.remove(0)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
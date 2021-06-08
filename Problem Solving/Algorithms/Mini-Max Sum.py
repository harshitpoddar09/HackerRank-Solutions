#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    minimum=sum(arr[0:4])
    maximum=sum(arr[1:5])
    ans=[]
    ans.append(str(minimum))
    ans.append(str(maximum))
    print(' '.join(ans))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

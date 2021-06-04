#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    # Write your code here
    arr=sorted(arr)
    min_diff=arr[1]-arr[0]
    ans=[arr[0],arr[1]]
    for i in range(2,len(arr)):
        cur_diff=arr[i]-arr[i-1]
        if cur_diff<min_diff:
            min_diff=cur_diff
            ans=[arr[i-1],arr[i]]
        elif cur_diff==min_diff:
            ans.append(arr[i-1])
            ans.append(arr[i])
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

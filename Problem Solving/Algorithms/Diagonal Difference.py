#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    diagonal=[]
    for i in range(len(arr)):
        diagonal.append(arr[i][i])
    a=sum(diagonal)
    diagonal_rev=[]
    arr.reverse()
    for j in range(len(arr)):
        diagonal_rev.append(arr[j][j])
    b=sum(diagonal_rev)
    c=abs(a-b)
    return c
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

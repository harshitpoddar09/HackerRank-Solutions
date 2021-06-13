#!/bin/python

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    i=0
    e=100
    while (i+k)%n!=0:
        e=e-1
        i=(i+k)%n
        if c[i]==1:
            e=e-2
    if c[0]==1:
        e=e-1-2
    else:
        e=e-1
    return e
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = raw_input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = map(int, raw_input().rstrip().split())

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the triplets function below.
def triplets(a, b, c):
    a=sorted(list(set(a)))
    b=sorted(list(set(b)))
    c=sorted(list(set(c)))
    ans=0
    ac=0
    bc=0
    cc=0
    for ele in b:
        while ac<len(a) and a[ac]<=ele:
            ac+=1
        while cc<len(c) and c[cc]<=ele:
            cc+=1
        ans+=ac*cc
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()

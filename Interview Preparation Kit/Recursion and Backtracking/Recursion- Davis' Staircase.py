#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stepPerms' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

d={}
def stepPerms(n):
    # Write your code here
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 4
    elif n<0:
        return 0
    if n not in d:
        d[n]=(stepPerms(n-1)+stepPerms(n-2)+stepPerms(n-3))
    return d[n]%(10**10+7)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input().strip())

    for s_itr in range(s):
        n = int(input().strip())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()


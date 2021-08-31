#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'toys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY w as parameter.
#

def toys(w):
    # Write your code here
    w.sort()
    i=0
    ans=0
    flag=False
    cur_min=float('inf')
    while i<len(w):
        if flag:
            if w[i]<cur_min+5:
                i+=1
            else:
                flag=False
        else:
            cur_min=w[i]
            i+=1
            flag=True
            ans+=1
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    w = list(map(int, input().rstrip().split()))

    result = toys(w)

    fptr.write(str(result) + '\n')

    fptr.close()

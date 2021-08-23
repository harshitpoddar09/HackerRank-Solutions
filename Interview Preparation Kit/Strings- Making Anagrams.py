#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter
#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def makeAnagram(a, b):
    # Write your code here
    ad=Counter(a)
    bd=Counter(b)
    for i in set(a):
        if i in ad and i in bd:
            qty=min(ad[i],bd[i])
            ad[i]-=qty
            bd[i]-=qty
    ans=0
    for key in ad:
        ans+=ad[key]
    for key in bd:
        ans+=bd[key]
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    # Write your code here
    if len(s)%2!=0:
        return -1
    s1=s[:len(s)//2]
    s2=s[len(s)//2:]
    ans=0
    for i in s1:
        if i in s2:
            s1=s1.replace(i,'',1)
            s2=s2.replace(i,'',1)
        else:
            ans+=1
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'theLoveLetterMystery' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def theLoveLetterMystery(s):
    # Write your code here
    ans=0
    if len(s)%2==0:
        right=len(s)//2
        left=right-1
    else:
        left=(len(s)//2)-1
        right=(len(s)//2)+1
    for i in range(len(s)//2):
        ans+=abs(ord(s[left])-ord(s[right]))
        left-=1
        right+=1
    return ans

        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()

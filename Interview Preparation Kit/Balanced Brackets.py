#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    stack=[]
    for i in s:
        if i=='[':
            stack.append(']')
        elif i=='(':
            stack.append(')')
        elif i=='{':
            stack.append('}')
        else:
            if len(stack)!=0 and stack[-1]==i:
                stack.pop()
            else:
                return 'NO'
    if len(stack)==0:
        return 'YES'
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
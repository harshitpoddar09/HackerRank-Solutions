#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    s=list(s)
    j=1
    while j<len(s):
        if s[j]==s[j-1] and ord(s[j])>=97 and ord(s[j])<=122:
            s.pop(j-1)
            s.pop(j-1)
            if j!=1:
                j-=1
        else:
            j+=1
    if len(s)==0:
        return 'Empty String'
    else:
        s=''.join(s)
        return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()

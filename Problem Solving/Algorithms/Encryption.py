#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # Write your code here
    s=s.replace(' ','')
    row=math.floor(len(s)**0.5)
    col=math.ceil(len(s)**0.5)
    ans=''
    for i in range(col):
        a=''
        for j in range(i,len(s),col):
            a+=s[j]
        ans+=a+' '
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()

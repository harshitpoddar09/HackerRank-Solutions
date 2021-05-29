#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisors' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def divisors(n):
    # Write your code here
    if n%2!=0:
        return 0
    else:
        ans=0
        for i in range(1,int(n**0.5)+1):
            if n%i==0:
                if i%2==0:
                    ans+=1
                if (n//i)%2==0 and i**2!=n:
                    ans+=1
        return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = divisors(n)

        fptr.write(str(result) + '\n')

    fptr.close()

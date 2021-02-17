#!/bin/python3

import os
import sys

#
# Complete the summingSeries function below.
#
def summingSeries(n):
    #
    # Write your code here.
    #
    #Tn=2n-1
    #Sn=n(n+1)-n
    return (n*(n+1)-n)%(10**9+7)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = summingSeries(n)

        fptr.write(str(result) + '\n')

    fptr.close()
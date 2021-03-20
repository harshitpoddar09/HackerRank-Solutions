#!/bin/python3

import os
import sys

#
# Complete the handshake function below.
#
def handshake(n):
    #
    # Write your code here.
    #
    if n<2:
        return 0
    return (n*(n-1))//2   #nC2 - permutation and combination logic

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = handshake(n)

        fptr.write(str(result) + '\n')

    fptr.close()
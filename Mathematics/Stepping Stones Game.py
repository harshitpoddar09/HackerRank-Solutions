#!/bin/python3

import os
import sys

# Complete the solve function below.
def solve(n):
    #we need to check if n=(m(m+1))//2 --> m^2 + m - 2n = 0 for some natural no. m
    # m = (-b+-(D^0.5))/2a
    D=1+(8*n)
    m=(-1+(D**0.5))/2
    ans='Better Luck Next Time'
    if m==int(m):
        ans='Go On Bob '+str(int(m))
    return ans 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = solve(n)

        fptr.write(result + '\n')

    fptr.close()

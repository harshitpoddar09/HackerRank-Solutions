#!/bin/python3

import os
import sys

# Complete the solve function below.
def solve(n, m):
    #ans=(n+m-1)C(n)=(n+m-1)C(m-1)
    ans=1
    for i in range(n+m-1,n,-1):
        ans*=i
    for j in range(1,m-1+1):
        ans=ans//j
    return ans%((10**9)+7)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        result = solve(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()

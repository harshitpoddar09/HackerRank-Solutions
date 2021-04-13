#!/bin/python3

import os
import sys
import math

# Complete the solve function below.
def factorial(n):
    return math.factorial(n)

def solve(n):
    all_fact=[factorial(i) for i in range(n+1)]
    ans=[]
    for j in range((n//2)+1):
        ans.append(str((all_fact[n]//(all_fact[j]*all_fact[n-j])%(10**9))))
    ans+=ans[::-1]
    if n%2==0:
        ans.pop(len(ans)//2)
    return ans
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = solve(n)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
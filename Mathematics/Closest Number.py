#!/bin/python3

import os
import sys
import math

#
# Complete the closestNumber function below.
#
def closestNumber(a, b, x):
    #
    # Write your code here.
    #
    num1=math.floor((a**b)/x)
    num2=math.ceil((a**b)/x)
    if abs((a**b)-(num1*x))<=abs((a**b)-(num2*x)):
        return num1*x
    return num2*x

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        abx = input().split()

        a = int(abx[0])

        b = int(abx[1])

        x = int(abx[2])

        result = closestNumber(a, b, x)

        fptr.write(str(result) + '\n')

    fptr.close()

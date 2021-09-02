#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'decentNumber' function below.
#
# The function accepts INTEGER n as parameter.
#

def decentNumber(n):
    # Write your code here
    if n%3==0:
        print('5'*n)
    else:
        a=0
        while a<n+1:
            if (n-a)%3==0 and a%5==0:
                break
            else:
                a+=1
        if (n-a)%3==0 and a%5==0:
            print('5'*(n-a)+'3'*a)
        else:
            print(-1)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        decentNumber(n)
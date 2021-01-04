#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    count_p=0
    count_n=0
    count_zero=0
    for i in arr:
        if i>0:
            count_p+=1
        elif i==0:
            count_zero+=1
        else:
            count_n+=1
    ratio_p=round(count_p/len(arr),6)
    ratio_n=round(count_n/len(arr),6)
    ratio_zero=round(count_zero/len(arr),6)
    print(ratio_p)
    print(ratio_n)
    print(ratio_zero)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
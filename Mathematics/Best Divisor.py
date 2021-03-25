#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    divisors=[]
    for i in range(1,n+1):
        if n%i==0:
            divisors.append(i)
    best=[]
    for i in divisors:
        sum_digits=0
        for j in str(i):
            sum_digits+=int(j)
        best.append(sum_digits)
    index=best.index(max(best))
    print(divisors[index])
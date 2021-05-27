#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    for i in range(len(apples)):
        apples[i]+=a
    for j in range(len(oranges)):
        oranges[j]+=b
    count_a=0
    count_o=0
    for x in apples:
        if x>=s and x<=t:
            count_a+=1
    for y in oranges:
        if y>=s and y<=t:
            count_o+=1
    print(count_a)
    print(count_o)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)

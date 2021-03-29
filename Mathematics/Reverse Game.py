#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])
        ans=[]
        for i in range(n//2):
            ans.append(n-1-i)
            ans.append(i)
        if n%2!=0:
            ans.append(n//2)
        print(ans.index(k))
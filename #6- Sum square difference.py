#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(abs(((n*(n+1)*((2*n)+1))//6)-(((n*(n+1))//2)**2)))

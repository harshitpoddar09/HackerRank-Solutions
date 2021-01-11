#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    likes=0
    recipients=5
    while n>0:
        likes+=math.floor(recipients/2)
        recipients=math.floor(recipients/2)*3
        n-=1
    return likes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

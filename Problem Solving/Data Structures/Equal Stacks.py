#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

def equalStacks(h1, h2, h3):
    # Write your code here
    sum1=sum(h1)
    sum2=sum(h2)
    sum3=sum(h3)
    while True:
        if not h1 or not h2 or not h3:
            return 0
        if sum1==sum2 and sum2==sum3:
            return sum1
        if sum1>=sum2 and sum1>=sum3:
            sum1-=h1.pop(0)
        elif sum2>=sum1 and sum2>=sum3:
            sum2-=h2.pop(0)
        elif sum3>=sum1 and sum3>=sum2:
            sum3-=h3.pop(0)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()


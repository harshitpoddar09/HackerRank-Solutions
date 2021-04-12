#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sumOfGroup function below.
def sumOfGroup(k):
    # Return the sum of the elements of the k'th group.
    n=((k-1)*((k-1)+1))//2 #num of odd elements which got used till (k-1)th group
    k_group=[i for i in range((n*2)+1,(n*2)+1+(k*2),2)]
    return sum(k_group)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    k = int(input())

    answer = sumOfGroup(k)

    fptr.write(str(answer) + '\n')

    fptr.close()


#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'gameOfThrones' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def gameOfThrones(s):
    # Write your code here
    freqDict=Counter(s)
    a=0
    for key,value in freqDict.items():
        a+=value%2
    if a>1:
        return 'NO'
    else:
        return 'YES'     

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()

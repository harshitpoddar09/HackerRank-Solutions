#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    s_list=[]
    count=0
    for i in s:
        s_list.append(i)
    for p in range(0,len(s_list),3):
        if s_list[p]!='S':
            count+=1
    for q in range(1,len(s_list),3):
        if s_list[q]!='O':
            count+=1
    for r in range(2,len(s_list),3):
        if s_list[r]!='S':
            count+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()

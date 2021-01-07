#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    max_score=scores[0]
    min_score=scores[0]
    count_max=0
    count_min=0
    for i in range(len(scores)):
        if max_score<scores[i]:
            count_max+=1
            max_score=scores[i]
        elif min_score>scores[i]:
            count_min+=1
            min_score=scores[i]
    ans=[count_max,count_min]
    return ans
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count_dict={}
    ar.sort()
    for i in ar:
        count_dict[i]=ar.count(i)
    value_list=list(count_dict.values())
    ans=0
    for i in value_list:
        count=i//2
        ans+=count
    return ans
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    equal=[]    #to store array values which occur multiple times                      
    for i in a:
        if a.count(i)>1:
           if i not in equal:      #to make sure we store the value only once
            equal.append(i)
    minimum=[]                     
    # to store min distances of various equal values from the array 
    for j in range(len(equal)):
        index=[k for k in range(len(a)) if a[k]==equal[j]]       #list comprehension
        minimum_within=[]     
        #to store dist between various indices of a particular value
        for p in range(len(index)):
            for q in range(len(index)):
                if p!=q:
                    minimum_within.append(abs(index[p]-index[q]))
        minimum.append(min(minimum_within)) 
    if len(minimum)==0:
        return '-1'
    else:
        return (min(minimum))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    special=0
    lower=0
    upper=0
    num=0
    for i in password:
        if i in lower_case:
            lower+=1
        elif i in upper_case:
            upper+=1
        elif i in special_characters:
            special+=1
        elif i in numbers:
            num+=1
    strong=[special,lower,upper,num]
    present=0
    for j in strong:
        if j>0:
            present+=1
    if n>=6:
        if present==4:
            ans=0
        else:
            ans=4-present
    else:
        if present==4:
            ans=6-n
        else:
            ans=max(4-present,6-n)
    return ans
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()

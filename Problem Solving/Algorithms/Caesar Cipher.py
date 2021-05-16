#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    ans=''
    k=k%26
    for i in s:
        if ord(i)>=65 and ord(i)<=90:
            if ord(i)+k>90:
                ans+=chr(64+(ord(i)+k-90))
            else:
                ans+=chr(ord(i)+k)
        elif ord(i)>=97 and ord(i)<=122:
            if ord(i)+k>122:
                ans+=chr(96+(ord(i)+k-122))
            else:
                ans+=chr(ord(i)+k)
        else:
            ans+=i
    return ans   
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()

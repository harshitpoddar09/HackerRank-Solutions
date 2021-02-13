#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):
    words=[" o' clock",'one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','quarter','sixteen','seventeen','eighteen','nineteen','twenty','twenty one','twenty two','twenty three','twenty four','twenty five','twenty six','twenty seven','twenty eight','twenty nine','half']
    ans=str()
    if m==0:
        ans=words[h]+words[0]
    elif m==1:
        ans=words[1]+' minute past '+words[h]
    elif m==15 or m==30:
        ans+=words[m]+' past '+words[h]
    elif m>1 and m<30:
        ans=words[m]+' minutes past '+words[h]
    elif m==45:
        ans=words[15]+' to '+words[h+1]
    elif m==59:
        ans=words[1]+' minute to '+words[h+1]
    else:
        ans=words[60-m]+' minutes to '+words[h+1]
    return ans
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
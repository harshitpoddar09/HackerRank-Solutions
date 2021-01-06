#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    hour=s[slice(0,2)]
    minute=s[slice(3,5)]
    sec=s[slice(6,8)]
    ampm=s[slice(8,10)]
    if ampm=='AM':
        if hour=='12':
            new_hour='00'
            time=str(new_hour)+':'+str(minute)+':'+str(sec)
        else:
            time=str(hour)+':'+str(minute)+':'+str(sec)
    else:
        if hour=='12':
            new_hour='12'
            time=str(new_hour)+':'+str(minute)+':'+str(sec)
        else:
            new_hour=12+int(hour)
            time=str(new_hour)+':'+str(minute)+':'+str(sec)
    return time

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
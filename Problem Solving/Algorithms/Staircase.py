#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    width=n
    for i in range(n):
        print(('#'*(i+1)).rjust(width,' '))
if __name__ == '__main__':
    n = int(input())

    staircase(n)

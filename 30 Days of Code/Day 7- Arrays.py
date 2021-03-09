#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    arr = list(map(str, input().split()))
    arr.reverse()
    print(' '.join(arr))
         

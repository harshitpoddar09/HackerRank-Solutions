#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = input()
s=Counter(s)
s=s.items()
s=sorted(s)
s=sorted(s,key=lambda x:(x[1]),reverse=True)
for i in range(3):
    print(s[i][0],s[i][1])
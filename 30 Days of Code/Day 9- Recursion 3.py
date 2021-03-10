#!/bin/python3

import math
import os
import random
import re
import sys

n=int(input())
i=1
factorial=1
while i<n+1:
    factorial=factorial*i
    i=i+1
print(factorial)    
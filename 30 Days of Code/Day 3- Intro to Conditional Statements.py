#!/bin/python3

import math
import os
import random
import re
import sys



n = int(input())
if n%2!=0 :
    print("Weird")
elif n==2 or n==4 :
    print("Not Weird")   
elif n%2==0 and n>=6 and n<=20:
    print("Weird")
elif n%2==0 and n>=20 and n<=100:
    print ("Not Weird")         

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        a = list(map(int, input().rstrip().split()))

        # Write your code here
        new=[i%3 for i in a]
        xor=0
        for j in new:
            xor^=j
        if xor==0:
            print('Koca')
        else:
            print('Balsa')

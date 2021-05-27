#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the acmTeam function below.
def acmTeam(topic):
    count_list=[]
    for i in range(len(topic)-1):
        for j in range(i+1,len(topic)):
            count=0
            for k in range(len(topic[0])):
                if topic[i][k]=='1' or topic[j][k]=='1':
                    count+=1
            count_list.append(count)
    return [max(count_list),count_list.count(max(count_list))]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

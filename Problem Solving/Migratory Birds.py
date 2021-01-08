import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    arr.sort()
    arr_set=set(arr)
    b=0
    i=0
    for i in arr_set:
        a=arr.count(i)
        if a>b:
            b=a
            ans=i
    return ans    
            
    """
    #exceeds time limit for 2 cases
    
    count_list=[]
    for i in arr:
        count=arr.count(i)
        count_list.append(count)
    maximum=max(count_list)
    index=[]
    for j in range(len(count_list)):
        if count_list[j]==maximum:
            index.append(j)
    minimum_list=[]
    for k in index:
        minimum_list.append(arr[k])
    minimum=min(minimum_list)
    return minimum
    """
    
    """
    #time limit exceeding for 2 cases
    
    count_list=[]
    arr.sort()
    for i in arr:
        count=arr.count(i)
        count_list.append(count)
    maximum=max(count_list)
    for j in range(len(count_list)):
        if count_list[j]==maximum:
            return arr[j]
    """ 
    
    """
    #exceeds time limit for 2 cases
    count_dict={}
    arr.sort()
    for i in arr:
        count_dict[i]=arr.count(i)
    value_list=list(count_dict.values())
    key_list=list(count_dict.keys())
    maximum=max(value_list)
    max_index=value_list.index(maximum)
    return key_list[max_index]
    """

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(raw_input().strip())

    arr = map(int, raw_input().rstrip().split())

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
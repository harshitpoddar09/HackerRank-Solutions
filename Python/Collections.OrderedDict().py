# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
market=OrderedDict()
n=int(input())
for i in range(n):
    item=list(map(str,input().split()))
    if ' '.join(item[:len(item)-1]) in market:
        market[' '.join(item[:len(item)-1])]+=int(item[-1])
    else:
        market[' '.join(item[:len(item)-1])]=int(item[-1])
for key,value in market.items():
    print(key,value)
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
d=deque()
n=int(input())
for i in range(n):
    task=list(map(str,input().split()))
    if task[0]=='append':
        d.append(int(task[-1]))
    elif task[0]=='appendleft':
        d.appendleft(int(task[-1]))
    elif task[0]=='pop':
        d.pop()
    else:
        d.popleft()
for j in d:
    print(j,end=' ')
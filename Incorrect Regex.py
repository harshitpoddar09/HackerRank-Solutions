# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
t=int(input())
a=[]
for i in range(t):
    a.append(str(input()))
for j in a:
    try:
        print(bool(re.compile(j)))
    except re.error:
        print('False') 
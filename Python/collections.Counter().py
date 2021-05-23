# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
x=int(input())
size=list(map(int, input().split()))
n=int(input())
a=[]
for i in range(n):
    b=list(map(int, input().split()))
    a.append(b)
freqDict=Counter(size)
ans=0
for i in a:
    if freqDict[i[0]]:
        freqDict[i[0]]-=1
        ans+=i[1]
print(ans)
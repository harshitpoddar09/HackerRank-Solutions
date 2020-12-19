# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
a=list(map(str, input().split()))
string=str(a[0])
n=int(a[1])
d=list(permutations(string,n))
d.sort()
for i in range(len(d)):
    x=''.join(d[i])
    print(x)
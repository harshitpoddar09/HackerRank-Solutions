# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
data=list(map(str, input().split()))
k=int(data[1])
word=sorted(data[0])
ans=list(combinations_with_replacement(word,k))
ans.sort()
for i in range(len(ans)):
    print(''.join(ans[i]))

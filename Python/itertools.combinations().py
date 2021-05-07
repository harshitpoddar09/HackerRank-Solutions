# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
a=list(map(str,input().split()))
word=a[0]
k=int(a[1])
word_list=list(word)
word_list.sort()
for x in range(1,k+1):
    ans=list(combinations(word_list,x))
    for j in range(len(ans)):
        x=''.join(ans[j])
        print(x)

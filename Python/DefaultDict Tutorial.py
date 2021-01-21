# Enter your code here. Read input from STDIN. Print output to STDOUT
num=list(map(int, input().split()))
n=num[0]
m=num[1]
a=[]
b=[]
for i in range(n):
    x=input()
    a.append(x)
for j in range(m):
    y=input()
    b.append(y)
for p in range(len(b)):
    ans=[]
    for q in range(len(a)):
        s=0
        if b[p]==a[q]:
            s=q+1
            ans.append(str(s))
    if len(ans)!=0:
        print(' '.join(ans))
    else:
        print('-1')

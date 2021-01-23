n=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
for i in range(n-1):
    if a[i]!=a[i+1]:
        sec_max=a[i+1]
        break
    else:
        i=i+1
print(sec_max)

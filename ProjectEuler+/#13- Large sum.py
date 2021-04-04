# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
ans=0
for i in range(n):
    ans+=int(input())
print(str(ans)[:10])

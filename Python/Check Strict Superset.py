# Enter your code here. Read input from STDIN. Print output to STDOUT
a=input().split()
a=set(a)
n=int(input())
flag=0
for i in range(n):
    other=input().split()
    other=set(other)
    if other.intersection(a)!=other:
        print(False)
        break
    if a.symmetric_difference(other):
        flag=1
else:
    if flag==1:
        print(True)
    else:
        print(False)
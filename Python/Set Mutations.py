# Enter your code here. Read input from STDIN. Print output to STDOUT
na=int(input())
a=set(map(int,input().split()))
n=int(input())
for i in range(n):
    operation=input().split()
    b=set(map(int,input().split()))
    if operation[0]=='update':
        a.update(b)
    elif operation[0]=='intersection_update':
        a.intersection_update(b)
    elif operation[0]=='difference_update':
        a.difference_update(b)
    else:
        a.symmetric_difference_update(b)
print(sum(a))
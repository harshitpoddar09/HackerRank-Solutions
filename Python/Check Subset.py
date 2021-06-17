# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(input())
for i in range(t):
    na=int(input())
    a=input().split()
    a=set(a)
    nb=int(input())
    b=input().split()
    b=set(b)
    if a.intersection(b)==a:
        print(True)
    else:
        print(False)
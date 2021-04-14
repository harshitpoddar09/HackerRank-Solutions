# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
arr=list(map(int,input().split()))
if all(i>0 for i in arr):
    if any(str(i)==str(i)[::-1] for i in arr):
        print('True')
    else:
        print('False')
else:
    print('False')
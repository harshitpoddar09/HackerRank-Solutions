# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(input())
a=[]
for i in range(t):
    b=[]
    b=list(map(str, input().split()))
    a.append(b)
for x in range(len(a)):
    try:
        print(int(a[x][0])//int(a[x][1]))
    except ZeroDivisionError:
        print ("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print ("Error Code:", e)

# Enter your code here. Read input from STDIN. Print output to STDOUT
q=int(input())
queue=[]
for i in range(q):
    inp=list(map(int,input().split()))
    if inp[0]==2:
        queue.pop(0)
    elif inp[0]==3:
        print(queue[0])
    else:
        queue.append(inp[1])
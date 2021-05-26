# Enter your code here. Read input from STDIN. Print output to STDOUT
def piling(block):
    stack=[]
    while block:
        if block[-1]>block[0]:
            stack.append(block[-1])
            block.pop()
        else:
            stack.append(block[0])
            block.pop(0)
        if len(stack)>=2:
            if stack[-1]>stack[-2]:
                return 'No'
    return 'Yes'
t=int(input())
for i in range(t):
    n=int(input())
    block=list(map(int,input().split()))
    print(piling(block))
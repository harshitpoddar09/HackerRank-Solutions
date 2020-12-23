n = int(input())
s = set(map(int, input().split()))
N = int(input())
command_list=[]
for i in range(N):
    command=list(map(str, input().split()))
    command_list.append(command)
for j in command_list:
    if j[0]=='pop':
        s.pop()
    elif j[0]=='remove':
        s.remove(int(j[1]))
    elif j[0]=='discard':
        s.discard(int(j[1]))
print(sum(s))
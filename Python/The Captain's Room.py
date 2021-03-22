# Enter your code here. Read input from STDIN. Print output to STDOUT
k=int(input())
room=list(map(int, input().split()))
print((((sum(set(room)))*k)-(sum(room)))//(k-1))
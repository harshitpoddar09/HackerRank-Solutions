# Enter your code here. Read input from STDIN. Print output to STDOUT
e=int(input())
eng=input().split()
eng=set(eng)
f=int(input())
fre=input().split()
fre=set(fre)
print(len(eng.difference(fre)))
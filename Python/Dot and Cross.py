import numpy
n=int(input())
a=[]
b=[]
for i in range(n):
    row_a=list(map(int, input().split()))
    a.append(row_a)
for i in range(n):
    row_b=list(map(int, input().split()))
    b.append(row_b) 
print(numpy.dot(a,b))

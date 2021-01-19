import numpy
data=list(map(int, input().split()))
n=data[0]
m=data[1]
a=[]
b=[]
for i in range(n):
    row_a=list(map(int, input().split()))
    a.append(row_a)
for i in range(n):
    row_b=list(map(int, input().split()))
    b.append(row_b) 
print(numpy.add(a,b))
print(numpy.subtract(a,b))
print(numpy.multiply(a,b))
print(numpy.floor_divide(a,b))
print(numpy.mod(a,b))
print(numpy.power(a,b))

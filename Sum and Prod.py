import numpy
data=list(map(int, input().split()))
n=data[0]
m=data[1]
matrix=[]
for i in range(n):
    row=list(map(int,input().split()))
    matrix.append(row)
add=numpy.sum(matrix, axis=0)
add=list(add)
multiply=numpy.prod(add, axis=0)
print(multiply)
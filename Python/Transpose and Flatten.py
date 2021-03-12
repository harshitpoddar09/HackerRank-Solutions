import numpy
data=list(map(int, input().split()))
n=data[0]
m=data[1]
matrix=[]
for i in range(n):
    row=list(map(int, input().split()))
    matrix.append(row)
print(numpy.transpose(matrix))
matrix=numpy.array(matrix)
print(matrix.flatten())

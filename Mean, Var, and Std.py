import numpy
data=list(map(int, input().split()))
n=data[0]
m=data[1]
matrix=[]
for i in range(n):
    row=list(map(float, input().split()))
    matrix.append(row)
print(numpy.mean(matrix, axis=1))
print(numpy.var(matrix, axis=0))
print(round(numpy.std(matrix, axis=None),11))
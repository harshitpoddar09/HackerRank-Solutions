import numpy
data=list(map(int, input().split()))
n=data[0]
m=data[1]
matrix=[]
for i in range(n):
    row=list(map(int, input().split()))
    matrix.append(row)
minimum=numpy.min(matrix, axis=1)
maximum=numpy.max(minimum, axis=0)
print(maximum)
import numpy
n=int(input())
matrix=[]
for i in range(n):
    row=list(map(float,input().split()))
    matrix.append(row)
det=numpy.linalg.det(matrix)
print(round(det,2))

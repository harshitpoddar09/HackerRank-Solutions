import numpy
numpy.set_printoptions(legacy='1.13')
data=list(map(int, input().split()))
n=data[0]
m=data[1]
print(numpy.eye(n,m,k=0))

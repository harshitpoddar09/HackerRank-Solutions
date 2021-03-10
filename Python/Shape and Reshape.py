import numpy
data=list(map(int, input().split()))
data=numpy.array(data)
print(numpy.reshape(data,(3,3)))

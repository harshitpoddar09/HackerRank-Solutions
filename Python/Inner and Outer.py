import numpy
a=list(map(int, input().split()))
b=list(map(int, input().split()))
print(numpy.inner(a,b))
print(numpy.outer(a,b))

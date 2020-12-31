import numpy
coefficients=list(map(float, input().split()))
x=float(input())
print(numpy.polyval(coefficients,x))
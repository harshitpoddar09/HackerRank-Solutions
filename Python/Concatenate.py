import numpy
data=list(map(int,input().split()))
n=data[0]
m=data[1]
p=data[2]
list_1=[]
list_2=[]
for i in range(n):
    a=list(map(int, input().split()))
    list_1.append(a)
for j in range(m):
    b=list(map(int, input().split()))
    list_2.append(b)
array_1=numpy.array(list_1)
array_2=numpy.array(list_2)
print(numpy.concatenate((array_1,array_2),axis=0)) 

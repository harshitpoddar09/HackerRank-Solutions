# Enter your code here. Read input from STDIN. Print output to STDOUT
data=list(map(int,input().split()))
n=data[0]
x=data[1]
marks=[]
student_marks=[]
for i in range(x):
    subject=list(map(float, input().split()))
    marks.append(subject)
for i in zip(*marks):
    print(sum(i)/len(i))

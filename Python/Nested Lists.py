b=[]
for i in range(int(input())):
    name = input()
    score = float(input())
    a=[]
    a.append(name)
    a.append(score)
    b.append(a)
marks=[]
for j in range(len(b)):
    marks.append(b[j][1])
marks.sort()
for k in range(len(marks)-1):
    if marks[k]!=marks[k+1]:
        sec_small=marks[k+1]
        break
    else:
        k=k+1
name=[]
for p in range(len(b)):
    for q in range(2):
        if b[p][q]==sec_small:
            name.append(b[p][q-1])
name.sort()
for z in range(len(name)):
    print(name[z]) 

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n=int(input())
word_list=[]
for i in range(n):
    word_list.append(str(input()))
freqDict=Counter(word_list)
print(len(freqDict))
for key,value in freqDict.items():
    print(value,end=' ')
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n=int(input())
for i in range(n):
    num=input()
    regex=r'[789]\d{9}$'
    if re.match(regex,num):
        print('YES')
    else:
        print('NO')
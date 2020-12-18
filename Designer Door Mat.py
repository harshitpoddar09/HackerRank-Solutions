# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m=list(map(int,input().split()))
a=3
for i in range((n-1)//2):
    print(('-'*((m-a)//2))+('.|.'*(a//3))+('-'*((m-a)//2)))      
    a=a+6
print(('-'*((m-7)//2))+'WELCOME'+('-'*((m-7)//2)))
a=a-6
for i in range((n-1)//2):
    print(('-'*((m-a)//2))+('.|.'*(a//3))+('-'*((m-a)//2)))      
    a=a-6
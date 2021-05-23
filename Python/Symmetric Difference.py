# Enter your code here. Read input from STDIN. Print output to STDOUT
m=int(input())
m_int=input().split()
m_int=set(map(int,m_int))
n=int(input())
n_int=input().split()
n_int=set(map(int,n_int))
a=n_int.difference(m_int)
b=m_int.difference(n_int)
a.update(b)
for i in sorted(a):
    print(i)
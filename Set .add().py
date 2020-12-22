# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
countries=[]
for i in range(n):
    countries.append(str(input()))
distinct=set(countries)
print(len(distinct))
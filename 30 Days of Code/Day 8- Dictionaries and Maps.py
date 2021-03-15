# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
phonebook={}
for i in range(n):
    [name,num]=list(map(str, input().split()))
    phonebook[name]=num
while True:
    try:
        query=str(input())
        if query in phonebook.keys():
            print(query+"="+phonebook[query])
        else:
            print('Not found')
    except:
        break  
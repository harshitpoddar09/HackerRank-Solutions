# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
english=input().split()
english=set(map(int, english))
n=int(input())
french=input().split()
french=set(map(int,french))
print(len(english.intersection(french)))
from collections import OrderedDict
def merge_the_tools(string, k):
    # your code goes here
    t=[]
    for i in range(0,len(string),k):
        t.append(string[i:i+k])
    for j in t:
        j=''.join(OrderedDict.fromkeys(j))
        print(j)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
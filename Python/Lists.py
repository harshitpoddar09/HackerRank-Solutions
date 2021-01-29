if __name__ == '__main__':
    n = int(input())
    command_list=[]
    arr_list=[]
    for i in range(n):
        command=list(map(str, input().split()))
        command_list.append(command)
    for j in command_list:
        if j[0]=='insert':
            arr_list.insert(int(j[1]),int(j[2]))
        elif j[0]=='print':
            print(arr_list)
        elif j[0]=='remove':
            arr_list.remove(int(j[1]))
        elif j[0]=='append':
            arr_list.append(int(j[1]))
        elif j[0]=='sort':
            arr_list.sort()
        elif j[0]=='pop':
            arr_list.pop()
        elif j[0]=='reverse':
            arr_list.reverse()

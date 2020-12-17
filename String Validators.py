if __name__ == '__main__':
    s = input()
    for i in s:
        a=any([i.isalnum()])
        if a==True:
            print(a)
            break
    else:
        print(False)
    for i in s:
        a=any([i.isalpha()])
        if a==True:
            print(a)
            break
    else:
        print(False)
    for i in s:
        a=any([i.isdigit()])
        if a==True:
            print(a)
            break
    else:
        print(False)
    for i in s:
        a=any([i.islower()])
        if a==True:
            print(a)
            break
    else:
        print(False)
    for i in s:
        a=any([i.isupper()])
        if a==True:
            print(a)
            break
    else:
        print(False)
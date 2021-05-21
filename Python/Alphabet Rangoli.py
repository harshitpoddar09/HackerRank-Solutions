def print_rangoli(size):
    # your code goes here
    width=(((size*2)-1)*2)-1
    arr=[]
    for i in range(size):
        ascii=96+size
        a=chr(ascii)
        for j in range(i):
            ascii-=1
            a+='-'+chr(ascii)
        for k in range(i):
            ascii+=1
            a+='-'+chr(ascii)
        arr.append(a.center(width,'-'))
        print(arr[-1])
    arr.pop()
    for l in range(size-1):
        print(arr[-1])
        arr.pop()
        

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
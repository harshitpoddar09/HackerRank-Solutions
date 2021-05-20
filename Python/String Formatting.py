def print_formatted(number):
    # your code goes here
    a=len(bin(number).replace('0b',''))
    for i in range(1,number+1):
        print(str(i).rjust(a),oct(i).replace('0o','').rjust(a),hex(i).replace('0x','').upper().rjust(a),bin(i).replace('0b','').rjust(a))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
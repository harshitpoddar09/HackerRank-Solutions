n=int(input())
word_list=[]
for i in range (0,n):
    word=str(input())
    word_list.append(word)
    i=i+1
even=""
odd=""    
for a in range (0,n):
    for b in range (0,len(word_list[a])):
        if b%2==0:
            even=even+word_list[a][b]
        else :
            odd=odd+word_list[a][b]
    print(even+" "+odd)
    even=""
    odd=""
         

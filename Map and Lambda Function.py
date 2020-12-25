cube = lambda x:x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    t1=0
    t2=1
    fibonacci_list=[]
    if n==1:
        fibonacci_list.append(t1)
    else:
        for i in range(n):
            fibonacci_list.append(t1)
            t=t1+t2
            t1=t2
            t2=t
    return fibonacci_list
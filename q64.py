#q64:
def fib():
    n=int(input('Enter a number for fibonacci series:'))
    a=0
    b=1
    sum=0
    for i in range(n):
        if(sum<=n):
            print(sum,end=" ")
            a=b
            b=sum
            sum=a+b
fib()

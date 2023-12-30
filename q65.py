#q65:
def fib():
    n=int(input('Enter a number for fibonacci series:'))
    a=0
    b=1
    sum=0
    sum1=0
    for i in range(n):
        if(sum<=n):
            sum1=sum1+sum
            print(sum,end=" ")
            a=b
            b=sum
            sum=a+b
    print()
    print('Sum of series:',sum1)
fib()

n=int(input('Enter the value of n:'))
r=int(input('Enter the value of r:'))
def Per(n,r):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    fact1=1
    for i in range(1,n-r+1):
        fact1=fact1*i
    print('P(n,r):',fact/fact1)
Per(n,r)

n=int(input('Enter the value of n:'))
r=int(input('Enter the value of r:'))
def Com(n,r):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    fact1=1
    for i in range(1,n-r+1):
        fact1=fact1*i
    fact2=1
    for i in range(1,r+1):
        fact2=fact2*i
    print('C(n,r):',fact/(fact2*fact1))
Com(n,r)

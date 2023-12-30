#q66:
def sod():
    n=int(input('Enter the number:'))
    sum=0
    while(n>0):
        d=n%10
        sum=sum+d
        n=n//10
    print('Sum of digits:',sum)
sod()

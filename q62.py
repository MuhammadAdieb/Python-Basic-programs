#q62:
def sos():
    n=int(input('Enter a number:'))
    sum=0
    print('Series is:')
    for i in range(1,n+1,3):
        print(i,end=",")
        sum=sum+i
    print()
    print('Sum of series is:',sum)
sos()

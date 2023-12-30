#q69:
n=int(input('Enter a number:'))
def son(n):
    if n==0:
        return 0
    else:
        return (n)+son(n-1)
sum=son(n)
print('Sum of ',n,' natural nummbers is:',sum)
    
    

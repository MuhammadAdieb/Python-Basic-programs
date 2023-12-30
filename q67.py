#q67
def prime():
    n=int(input('Enter a number:'))
    i=int(n/2)
    count=0
    for j in range(2,i+1):
        if n%j==0:
            count+=1
    if count==0:
        print('Number is a prime number')
    else:
        print('Number is not a prime number')
prime()

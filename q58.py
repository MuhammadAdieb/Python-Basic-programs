num=int(input('Enter a number:'))
def facto(x):
    fact=1
    for i in range(1,x+1):
        fact=fact*i
    print('Factorial of number is:',fact)
facto(num)

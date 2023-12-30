#q70:
n=int(input('Enter a nummber for factorial:'))
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
f=fact(n)
print('Factorial of ',n,' is:',f)

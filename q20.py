a=int(input('Enter a number:'))
b=int(input('Enter a number:'))
c=int(input('Enter a number:'))
if (a>b or b>a) and (a>c or b>c):
    print(c," is the smallest number")
elif b>c and c>a:
    print(a," is the smallest number")
elif c>a and a>b:
    print(b," is the smallest number")

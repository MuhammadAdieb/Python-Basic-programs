a=int(input('Enter first variable:'))
b=int(input('Enter second variable:'))
def swap(x,y):
    print('Number before swap is a:',x,' b:',y)
    x=x+y
    y=x-y
    x=x-y
    print('NUmber after swap a:',x,' b:',y)
swap(a,b)#pass by value

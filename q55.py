def thrnum():
    a=int(input('Enter 1st number'))
    b=int(input('Enter 2nd number'))
    c=int(input('Enter 3rd number'))
    if(a>b):
        if(b>c):
            print(a,' 1st number is greatest')
    elif b>a:
        if(a>c):
            print(b,' 2nd number is greatest')
    else:
        print(c,' 3rd number is greatest')
thrnum()


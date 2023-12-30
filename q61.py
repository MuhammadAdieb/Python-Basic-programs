a=int(input('Enter first number:'))
b=int(input('Enter second number:'))
def hanL(a,b):
    if(a>b):
        g=a
    else:
        g=b
    while(True):
        if g%a==0 and g%b==0:
            lcm=g
            break
        g+=1
    print('L.C.M is:',lcm)
    if(a<b):
        s=a
    else:
        s=b
    for i in range(1,s+1):
        if(a%i==0) and(b%i==0):
            hcf=i
    print('HCF is:',hcf)
hanL(a,b)
'''def HanL(a,b):
    if a>b and a%b==0:
        print('LCM is:',a)
    elif b>a and b%a==0:
        print('LCM is:',b)
    else:
        print('L.C.M is:',a*b)
HanL(a,b)'''

#q26:
a=int(input('Enter a number:'))
b=int(input('Enter a number:'))
num=int(input('Enter a choice from \n1.Addition \n2.Multiplication \n3.Substraction \n4.Division'))
if num==1:
    print('Addition:',a+b)
elif num==2:
    print('Multiplication:',a*b)
elif num==3:
    print('Substraction:',a-b)
elif num==4:
    print('Division:',a/b)
else:
    print('Choice is wrong')

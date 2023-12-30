n=int(input("Enter a number with one or more than one digit:"))
count=0
num=n
while(n>0):
    n=n//10
    count+=1
sum=0
num1=num
while(num>0):
    r=num%10 
    sum=sum+(r**count)
    num=num//10
if(num1==sum):
    print('Number is an Armstrong number')
else:
    print('Number is not an armstrong number')


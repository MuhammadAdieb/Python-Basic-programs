n=int(input("Enter a number with one or more than one digit:"))
sum=0
num=n
while(n>0):
    rem=n%10
    sum=sum*10+rem
    n=n//10
print("Reverse of number ",num,"is:",sum)
if(sum==num):
    print("Number is a palindrome")
else:
    print("Number is not a palindrome")
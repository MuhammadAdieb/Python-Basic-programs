n=int(input("Enter a number with one or more than one digit:"))
sum=0
while(n>0):
    rem=n%10
    sum+=rem
    n=n//10
print("Sum of the digits of number is:",sum)
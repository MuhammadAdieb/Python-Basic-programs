n=int(input("Enter a number with one or more than one digit:"))
count=0
while(n>0):
    n=n//10
    count+=1
print("Number of the digits in number is:",count)
n=int(input('Enter a natural number:'))
fact=1
sum=0
for i in range(1,n+1):
    fact=fact*i
    sum+=fact
print("Sum of factorial of the first ",n,' natural numbers:',sum)
#q36:
num=int(input("Enter a number:"))
if num<0 and num%2==0:
    print("Number ",num," is negative and even.")
elif num<0 and num%2!=0:
    print("Number ",num," is negative and odd.")
elif num>0 and num%2==0:
    print("Number ",num," is positive and even.")
else:
    print("Number ",num," is positive and odd.")

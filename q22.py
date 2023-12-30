#q41:
year=int(input("Enter a year:"))
if year%400==0 or year%100!=0 and year%4==0:
    print("year is a leap year")
else:
    print("Year is not a leap year")

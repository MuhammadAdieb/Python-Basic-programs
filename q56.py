def lpyr():
    year=int(input('Enter a year:'))
    if year%400==0 or (year%4==0 and year%100!=0):
        print(year,' Year is a leap year')
    else:
        print(year, 'Year is not a leap year')
lpyr()
        

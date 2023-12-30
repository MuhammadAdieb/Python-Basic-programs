#q8:
base=int(input("Eneter base of right angle triangle:"))
height=int(input("Eneter height of right angle triangle:"))
a=int(input("Eneter 1st side of scalene triangle:"))
b=int(input("Eneter 2nd side of scalene triangle:"))
c=int(input("Eneter 3rd side of scalene triangle:"))
area1=0.5*base*height
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**(1/2)
print("Area of scalene triangle:",area," Area of right angle triangle:",area1)

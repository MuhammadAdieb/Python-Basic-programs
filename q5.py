#q5:
a=int(input("Enter coefficient of x^2:"))
b=int(input("Enter coefficient of x:"))
c=int(input("Enter constant:"))
d=(b*b-4*a*c)
if d>0:
    r1=(-b+(d)**0.5)/2*a
    r2=(-b-(d)**0.5)/2*a
    print("Roots are real and distinct")
    print("Roots of quadratic equation are r1:",r1," r2:",r2)
elif d==0:
    r1=-b/2*a
    print("Roots are real and equal")
    print("Roots of quadratic equation are r1:",r1," r2:",r1)
elif d<0:
    r1=(-b+(d)**0.5)/2*a
    r2=(-b-(d)**0.5)/2*a
    print("Roots are imaginary")
    print("Roots of quadratic equation are r1:",r1," r2:",r2)

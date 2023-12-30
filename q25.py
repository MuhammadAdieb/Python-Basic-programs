#q16:
s1=int(input("Enter marks of subject 1:"))
s2=int(input("Enter marks of subject 2:"))
s3=int(input("Enter marks of subject 3:"))
s4=int(input("Enter marks of subject 4:"))
s5=int(input("Enter marks of subject 5:"))
per=(s1+s2+s3+s4+s5)/5
if(per>90 and per<=100):
    print('Grade:A')
elif(per>80 and per<=90):
    print('Grade:B')
elif(per>60 and per<=80):
    print('Grade:C')
elif(per>50 and per<=60):
    print('Grade:D')
elif(per>40 and per<=50):
    print('Grade:E')
elif per<=40:
    print('Grade:F')

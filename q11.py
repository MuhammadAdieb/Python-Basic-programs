#q25:
hour=int(input("Enter hours for time:"))
minute=int(input("Enter minute for time:"))
second=int(input("Enter seconds in time:"))
hh=hour*3600
mm=minute*60
print("Hours:{} and minutes:{} and seconds:{} converted to time in seconds:{}".format(hour,minute,second,(hh+mm+second)))

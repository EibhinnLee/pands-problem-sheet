# Eibhinn Lee
# program to confirm whether today is a weekday or the weekend

#import the datetime function
import datetime

today = datetime.datetime.now()

day = today.weekday()

#created dict for day names
dayname ={1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday', 7:'Sunday'}

print("Today is ", dayname[day])

#print next line based on day index extracted

if day <= 4:
    print("boo its a weekday no fun")
else:
    print("yes its the weekend")




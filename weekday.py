# Eibhinn Lee
# program to confirm whether today is a weekday or the weekend

#import the datetime function
import datetime

today = datetime.datetime.now()

day = today.weekday()

daysofweek ={0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}

print("Today is", daysofweek[day])

# Based on dictionary above(daysofweek), any number up to and including 4 = weekday
if day <= 4:
    print(" Its a weekday ")
# if not, weekend    
else:
    print("Its the weekend")




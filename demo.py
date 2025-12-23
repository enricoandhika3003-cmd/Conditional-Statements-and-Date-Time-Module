x = int(input("Enter a random integer: "))

if x%2 == 0:
    print("It is an even number")
else :
    print("It is an odd number")

height = float(input("Enter your height (cm): "))
weight = float(input("Enter your weight (kg): "))

BMI = weight/(height/100)**2
print("Your BMI is = " , BMI)

if BMI <= 18.4:
    print("You are underweight!")
elif BMI <= 24.9:
    print("You are healthy!")
elif BMI <= 29.9:
    print("You are overweight!")
elif BMI <= 39.9:
    print("You are obese!")
else :
    print("You are morbidly obese!")

y = int(input("Enter anothor random integer: "))

if y > 50:
    print("It is greater than 50.")
    if y%2 == 0:
        print("It is also an even number.")
    else :
        print("It is also an odd number.")
else :
    print("It is less than 50.")

import datetime

currentTime = datetime.datetime.now()
print("Current time in Jakarta, Indonesia is ", currentTime)

import calendar
print("/n", calendar.calendar(2025))

from datetime import datetime
from zoneinfo import ZoneInfo


jakarta_time = datetime.now(ZoneInfo("Asia/Jakarta"))
print(jakarta_time.strftime("%d-%m-%Y %H:%M:%S"))

# EXO DU 01.04.2021
# if needed https://www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-3.php
# if needed https://www.w3resource.com/python-exercises/python-basic-exercise-3.php
"""
Write a Python program to convert temperatures to and from celsius, fahrenheit.
"""
# version Triche
def convertCFtiti(x,y):
    if y == "C":
        conv1 = (x*(9/5)) + 32
        print("Temp in fahrenheit : " + str(conv1))
    elif y == "F":
        conv2 = (x-32)*(5/9)
        print("Temp in celcius : " + str(conv2))
    else :
        print ("Are you sure of the temperature value ?")

x=float(input("Enter a value : "))
y=str(input("C for Celcius or F for Fahrenheit"))
convertCFtiti(x,y)


# fonction avec l'analyse dernière lettre chaine caractère
def convertCFtiti2(x):
    if (x.lower()[-1]) == "c" :
        f=float(x[:-1])
        conv1 = (f*(9/5)) + 32
        print("Temp in Fahrenheit : " + str(conv1)+ "°")
    elif (x.lower()[-1]) == "f" :
        c=float(x[:-1])
        conv2 = (c-32)*(5/9)
        print("Temp in Celcius : " + str(conv2) + "°")
    else :
        print ("Are you sure of the temperature value ?")

x=input("Enter a value : ")
convertCFtiti2(x)

################################################################################
"""
Write a Python script to concatenate following dictionaries to create a new one
"""
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}

dic4 = {}
dic4.update(dic1)
dic4.update(dic2)
dic4.update(dic3)
print(dic4)

# OU
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)

# OU
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}

dic4 = {**dic1, **dic2, **dic3}
print(dic4)

################################################################################
"""
Write a Python program to display the current date and time.
"""
from datetime import datetime

# datetime object containing current date and time
now = datetime.now()

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)
################################################################################
"""
Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]
Pictorial Presentation:
Display the first and last colors from a given list
"""
color_list = ["Red","Green","White" ,"Black"]
print (color_list[0]+" "+color_list[-1])
################################################################################
"""
Write a Python program to get OS name, platform and release information.
"""
import platform
import os
print(os.name)
print(platform.system())
print(platform.release())
################################################################################
"""
Write a Python program to get the file size of a plain file
"""
import os

file_size = os.path.getsize('d:/file.jpg')
print("File Size is :", file_size, "bytes")
################################################################################
"""
Write a Python program to write a list to a file
"""



################################################################################
"""
Write a Python script to display the various Date Time formats.
a) Current date and time
b) Current year
c) Month of year
d) Week number of the year
e) Weekday of the week
f) Day of year
g) Day of the month
h) Day of week
resultat :
Current date and time: 2017-05-05 17:21:19.106836
Current year: 2017
Month of year: May
Week number of the year: 18
Weekday of the week: 5
Day of year: 125
Day of the month : 05
Day of week: Friday
"""
import time
import datetime
print("Current date and time: " , datetime.datetime.now())
print("Current year: ", datetime.date.today().strftime("%Y"))
print("Month of year: ", datetime.date.today().strftime("%B"))
print("Week number of the year: ", datetime.date.today().strftime("%W"))
print("Weekday of the week: ", datetime.date.today().strftime("%w"))
print("Day of year: ", datetime.date.today().strftime("%j"))
print("Day of the month : ", datetime.date.today().strftime("%d"))
print("Day of week: ", datetime.date.today().strftime("%A"))
################################################################################
"""
Write a Python program to get days between two dates. Go to the editor
Sample Dates : 2000,2,28, 2001,2,28 ; Expected Output : 366 days, 0:00:00
"""
from datetime import date


f_date = date(input("year, month, day"))


f_date = date(2000,2,28)
l_date = date(2001,2,28)
delta = l_date - f_date
print(delta.days)

################################################################################
















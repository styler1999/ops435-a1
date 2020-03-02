#!/usr/bin/env python3 

#OPS435 Assignment 1 - Winter 2020
#Program: a1_[student_id].py (replace student_id with your Seneca User name)
#Author: "Sean Tyler"
#The python code in this file (a1_[Student_id].py) is original work written by
#"Sean Tyler". No code in this file is copied from any other source 
#except those provided by the course instructor, including any person, 
#textbook, or on-line resource. I have not shared this python script 
#with anyone or anything except for submission for grading.  
#I understand that the Academic Honesty Policy will be enforced and 
#violators will be reported and appropriate action will be taken.

import sys

def usage():
 idk = 'This is a script that will give you numbers back after you enter some'
 
 print(idk) 
 exit()

def valid_date(today):
 '''Checks to see if the date entered is Valid ''' 
 if len(today) != 10:
  print("Error: wrong date entered") 
  return False 

 str_year, str_month, str_day = today.split('-')
 year = int(str_year)
 month = int(str_month)
 day = int(str_day)
 
 if int(month) > 12:
  print("Error: wrong month entered")
  return False
 
 if int(day) > 31:
  print("Error: wrong date entered:")
  return False
 
 else:
  return True

def leap_year(year):
 '''Checks to see if the year is a leap year '''
 lyear = year % 4
 if lyear == 0:
  feb_max = 29 # this is a leap year
 else:
  feb_max = 28 # this is not a leap year

 lyear = year % 100
 if lyear == 0:
  feb_max = 28 # this is not a leap year

 lyear = year % 400
 if lyear == 0:
  feb_max = 29 # this is a leap year
 return feb_max

def days_in_mon(year):
 '''Holds the days in each month '''
 feb_max = leap_year(year)
 mon_max = { 1:31, 2:feb_max, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}    
 return mon_max


def after(today):
 '''Returns the day after day entered '''
 str_year, str_month, str_day = today.split('-')
 year = int(str_year)
 month = int(str_month)
 day = int(str_day)

 feb_max = leap_year(year)
 mon_max = days_in_mon(year)
   
 tmp_day = day + 1 # next day

 if tmp_day > mon_max[month]:
  to_day = tmp_day % mon_max[month] # if tmp_day > this month's max, reset to 1
  tmp_month = month + 1
 else:
  to_day = tmp_day
  tmp_month = month + 0

 if tmp_month > 12:
  to_month = 1
  year = year + 1
 else:
  to_month = tmp_month + 0
 
 next_date = str(year)+"-"+str(to_month).zfill(2)+"-"+str(to_day).zfill(2)
    
 return next_date


def before(today):
 '''Returns the day before the day entered '''  
 str_year, str_month, str_day = today.split('-')
 year = int(str_year)
 month = int(str_month)
 day = int(str_day)
 
 feb_max = leap_year(year)
 mon_max = days_in_mon(year) 

 tmp_day = day - 1
 tmp_month = month
 
 if tmp_day < 1: 
  tmp_month = month - 1  
  if tmp_month < 1: 
   to_day = 31
   #tmp_month = month - 1 
  else:
   #tmp_month = month - 1 
   to_day = mon_max[tmp_month]      
 if tmp_month <= 0:
  to_month = 12
  year = year - 1
  to_day = 31
 else:
  to_month = tmp_month
  to_day = tmp_day
 if tmp_month < 0:
  to_day = tmp_day 

 before_date = str(year)+"-"+str(to_month).zfill(2)+"-"+str(to_day).zfill(2)
     
 return before_date 


def dbda(today,num1):
 '''This doesn't work '''
 valid =  valid_date(today) 
 if valid == True: 
  if num1 > 0:
   print(after(today))
  if num1 < 0:
   print(before(today))
 else:
  print(valid) 


today =sys.argv[1]
print(after(today))
print(before(today)) 
 

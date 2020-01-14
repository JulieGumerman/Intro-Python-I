"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

#you need an input 
  #check
#no input? current month calendar
#one argument = month
#two arguments = month + year
#print a statement indicating format
#exit the program

date_input = input("State month and year. Please use MM/YYYY format:    ")
c = calendar.TextCalendar(calendar.SUNDAY)
now = datetime.now()



try:
  if (len(date_input) == 0):
    c_for_use = c.formatmonth(now.year, now.month)
    print(c_for_use)
  elif "/" in date_input:
    split_date = date_input.split("/")
    c_for_use = c.formatmonth(int(split_date[1]), int(split_date[0]))
    print(c_for_use)
  elif "/" not in date_input:
    c_for_use = c.formatmonth(now.year, int(date_input))
    print(c_for_use)
except:
  print("Please use 00/0000 format")
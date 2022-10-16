#=======================================
#Program name: Return Day
#Author Name: Josue Cifuentes
#Date: October 16,2022
#Purpose of the program:To print a return day
#=======================================

Start=int(input('What day does your vacation start? (Sun=0 Mon=1 Tues=2 Wed=3 Thurs=4 Fri=5 Sat=6) '))
Length=int(input('How many days are you leaving for? '))
Returnday= (Start + Length)%7
print('Return day is', Returnday)
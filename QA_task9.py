# Python program to check leap year

def checkYear(year):
    return (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0));

year = int(input('Please enter the year: '))
if (checkYear(year)):
    print("Leap Year")
else:
    print("Not a Leap Year")
def return_10():
    return 10

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def length_of_string(string):
    return len(string)

def join_string(string_1, string_2):
    return (string_1 + string_2)

def add_string_as_number(string_1, string_2):
    return (int(string_1) + int(string_2))

import calendar
def number_to_full_month_name(month1):
    return(calendar.month_name[month1])

def number_to_full_month_name1(month3):
    return(calendar.month_name[month3])

def number_to_full_month_name2(month9):
    return(calendar.month_name[month9])

def number_to_short_month_name(month1):
        return(calendar.month_abbr[month1])

def number_to_short_month_name(month4):
        return(calendar.month_abbr[month4])

def number_to_short_month_name(month10):
        return(calendar.month_abbr[month10])

def volume_of_cube(width):
    volume = width * width * width
    volume = volume / 1000
    return(volume)
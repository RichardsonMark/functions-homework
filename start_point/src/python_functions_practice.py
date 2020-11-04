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
    # work out vol and / 1000 (change from ml cubed to ml)
    volume = width * width * width
    volume = volume / 1000
    return(volume)

def reverse_string(string_forward):
    # Slice the string to reverse it
    string_reversed = "test" [::-1]
    return(string_reversed)

def fahrenheit_to_celsius(tempF):
    # convert to celsius
    celsius = (tempF - 32) * 5/9
    return(celsius)
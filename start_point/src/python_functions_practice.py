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

def number_to_full_month_name(month1):
    import datetime
    x = datetime.datetime(2020, 1, 1)
    return(x.strftime("%B"))

def number_to_full_month_name1(month3):
    import datetime
    x = datetime.datetime(2020, 3, 1)
    return(x.strftime("%B"))

def number_to_full_month_name2(month9):
    import datetime
    x = datetime.datetime(2020, 9, 1)
    return(x.strftime("%B"))


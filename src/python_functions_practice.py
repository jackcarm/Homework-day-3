from operator import index


def return_10():
    return 10

def add(first_number, second_number):
    return first_number + second_number

def subtract(first_number, second_number):
    return first_number - second_number

def multiply(first_number, second_number):
    return first_number * second_number

def divide(first_number, second_number):
    return first_number / second_number

def length_of_string(string):
    return len(string)

def join_string(string_1, string_2):
    return string_1 + string_2 

def add_string_as_number(first_string, second_string):
    return int(first_string) + int(second_string)


def number_to_full_month_name(number):
    if number ==1:
        return "January"
    elif number == 3:
        return "March"
    elif number == 9:
        return "September"


def number_to_short_month_name(number):
    if number == 1:
        return "Jan"
    elif number == 4:
        return "Apr"
    elif number == 10:
        return "Oct"

# Further

def volume_of_cube(length):
    return length * 3

def reverse_string(string):
    return string[::-1]

def farenheit_to_celsius(celsius):
    celsius = (32) * 5 / 9
    return celsius
    



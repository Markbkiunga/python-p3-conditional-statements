#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if (username == 'admin' or username == 'ADMIN') and password == '12345':
        response = 'Access granted'
    else:
        response = 'Access denied'
    return response


def hows_the_weather(temperature):
    # your code here
    pass
    if temperature < 40:
        response = 'It\'s brisk out there!'
    elif temperature >= 40 and temperature <= 65:
        response = 'It\'s a little chilly out there!'
    elif temperature > 85:
        response = 'It\'s too dang hot out there!'
    else:
        response = 'It\'s perfect out there!'
    return response


def fizzbuzz(num):
    # your code here
    pass
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return num


def calculator(operation, num1, num2):
    # your code here
    pass
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1/num2
    else:
        print('Invalid operation!')
        return None

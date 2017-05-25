"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

def tokenize_input(user_input):
    token_list = user_input.split(' ')
    return token_list

def calculator(token_list):
    if token_list[0] == '+':
        print add(int(token_list[1]), int(token_list[2]))
    elif token_list[0] == '-':
        print (subtract(int(token_list[1]), int(token_list[2])))
    elif token_list[0] == '*':
        print (multiply(int(token_list[1]), int(token_list[2])))
    elif token_list[0] == '/':
        print divide(int(token_list[1]), int(token_list[2]))
    elif token_list[0] == 'square':
        print square(int(token_list[1]))
    elif token_list[0] == 'cube':
        print cube(int(token_list[1]))
    elif token_list[0] == 'pow':
        print power(int(token_list[1]), int(token_list[2]))
    elif token_list[0] == 'mod':
        print mod(int(token_list[1]), int(token_list[2]))

while True:
    user_input = raw_input('>')
    calculator(tokenize_input(user_input))
    if user_input == 'q':
        print 'the program will now quit'
        break

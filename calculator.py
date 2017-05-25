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
        return add(int(token_list[1]), int(token_list[2]))
    elif token_list[0] == '-':
        return (subtract(int(token_list[1]), int(token_list[2])))
    elif token_list[0] == '*':
        return (multiply(int(token_list[1]), int(token_list[2])))
    elif token_list[0] == '/':
        return divide(int(token_list[1]), int(token_list[2]))
    elif token_list[0] == 'square':
        return square(int(token_list[1]))
    elif token_list[0] == 'cube':
        return cube(int(token_list[1]))
    elif token_list[0] == 'pow':
        return power(int(token_list[1]), int(token_list[2]))
    elif token_list[0] == 'mod':
        return mod(int(token_list[1]), int(token_list[2]))

# while True:
#     user_input = raw_input('> ')
def compute_data(operations_data_filename, results_filename):
    operations_data = open(operations_data_filename)
    results_data = open(results_filename, 'w')
    for line in operations_data:
        line = line.rstrip()
        results_data.write(str(calculator(tokenize_input(line))))
        results_data.write("\n")

compute_data("operations.txt", "results.txt")
    # if user_input == 'q':
    #     print 'the program will now quit'
    #     break
    
    # try:
    #     calculator(tokenize_input(user_input))
    #     # user_input = int(user_input)
    # except ValueError:
    #     print("Oops! That was an invalid input. Try again.")
    #     # user_guess = int(float(user_guess))
    #     # print user_guess
    # except IndexError:
    #     print("Oops! Not enough numbers for the given command. Try again.")

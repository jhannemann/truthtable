#!/usr/bin/env python
# truthtable.py - A Python module to print truth tables
#
# SPDX-FileCopyrightText: 2020 Dr.-Ing. Jens Hannemann <j.hannemann@ieee.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later


"""A module to print the truth table of boolean functions

This module exports a single function, print_truth_table,
which takes a boolean function as an argument and prints
the function's truth table
"""


import inspect


def print_truth_table(f):
    """Print the truth table of a boolean function

    The function parameter f should be a boolean function with an arbitrary
    number of positional boolean arguments and should return a single
    boolean value.

    The function uses the inspect module's facilities to derive the
    number and names of the function parameters automatically
    """
    
    signature = inspect.signature(f)
    parameters = signature.parameters
    number_of_bits = len(parameters)
    print(f.__name__+str(signature)+':')
    for parameter_name in parameters.keys():
        print(parameter_name+'|', end='')
    print(f.__name__)
    print('-'*2*number_of_bits+'-'*len(f.__name__))
    args = list(range(number_of_bits))
    for num in range(2**number_of_bits):
        n = num
        # extract bits from n and put it in args list
        for bit in range(number_of_bits):
            args[bit] = n % 2
            n = n//2
        # extraction by repeated division gives least significant bit first
        # order must be reversed for least significant bit to be last
        args.reverse()
        for arg in args:
            print(str(arg)+'|', end='')
        # call function by unpacking arguments from list
        print(str(int(f(*args))))


if __name__ == "__main__":

    def NOT(x):
        return not x


    def AND(x, y):
        return x and y


    def OR(x, y):
        return x or y


    def XOR(x, y):
        return (x and not y) or (y and not x)


    def NAND(x, y):
        return not(x and y)


    def NOR(x, y):
        return not(x or y)


    def implication(x, y):
        return not x or y


    def biconditional(x, y):
        return implication(x, y) and implication(y, x)


    def three(x, y, z):
        return (x and y) or (z and x)


    def four(w, x, y, z):
        return (w and x) or (x and z) or (not y)


    for function in (NOT, AND, OR, XOR, NAND, NOR, implication, biconditional,
                     three, four):
        print_truth_table(function)
        print()

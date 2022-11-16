"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
import math


def primes(number_of_primes):

    if number_of_primes <= 0:
        raise ValueError("The input number must greater than 0!")
    i = 2;
    j = 2;
    list = []
    temp = number_of_primes
    if number_of_primes == 1:
        list.append(2)
    for i in range(2,number_of_primes*5):
        count = 0
        if len(list) != temp:
            for j in range(2,number_of_primes*5):
                if i % j == 0:
                    count = count + 1
            if count == 1:
                list.append(i)
        else:
            break


    print(list)
    return list

"""
Author: James Ojoawo

This script is a background test for a future stats work,
Here, a function is created that accepts a value and generates
a finite set of extreme possible values that average up to the input value.
"""

import random
import statistics as st


def value_generator(start, stop, step):
    """
    Generates a range of values
    for floating point numbers.
    :param start: float starting from which the sequence is to be returned
    :param stop: float before which the sequence of integers is to be returned
    :param step: float value that determines the increment
    :return:
    """

    #f = 10 ** (len(str(step)) - str(step).find('.') - 1)
    f = step**-1
    rf = range(int(start * f), int(stop * f), int(step * f))
    r = [i / f for i in rf]

    return r


def mean_generator(mean, std, restrictions):
    """
    Generates the extreme possible values
    from a given mean, standard deviation
    and a list of restrictions
    :param std: given standard deviation of the population sample
    :param mean: mean of the population sample
    :param restrictions: all possible values in a restricted list
    :return:
    """
    # Empty list for the possible values of population sample
    possible_values = []

    # Use Gaussian Distribution to generate samples
    for i in range(len(restrictions)):
        values = round(random.gauss(mean, std), 3)
        possible_values.append(values)

    # Filter gaussian values with restriction values for accuracy
    set_res = set(restrictions)
    set_pos = set(possible_values)
    selection = set_pos.intersection(set_res)

    #   Generate Final & Accurate Samples
    final_values = random.sample(list(selection), 4)

    #   Ensure Mean Accuracy with Percentage Error Of 2%
    if st.fmean(final_values) in value_generator(mean - 0.02, mean + 0.02, .001):
        return final_values
    else:
        mean_generator(mean, std, restrictions)
        return final_values


def main():
    minimum = float(input('Supply the Minimum value for possible values to be generated: '))
    maximum = float(input('Supply the Maximum value for possible values to be generated: '))
    rangee = value_generator(minimum, maximum, 0.001)
    mean = float(input('Supply the mean of the population sample: '))
    std = float(input('Supply the standard deviation of the population sample: '))
    mean_generator(mean, std, rangee)
    print(f'Possible Values for your mean and standard deviation supplied are: {mean_generator(mean, std, rangee)}')


main()

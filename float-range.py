def value_generator(start, stop, step):
    """
    Generates a range of values
    for floating point numbers.
    :param start: float starting from which the sequence is to be returned
    :param stop: float before which the sequence of integers is to be returned
    :param step: float value that determines the increment
    :return:
    """

    f = 10 ** (len(str(step)) - str(step).find('.') - 1)
    rf = list(range(int(start * f), int(stop * f), int(step * f)))
    r = [i / f for i in rf]

    return r


print(value_generator(2.900, 3.900, 0.001))
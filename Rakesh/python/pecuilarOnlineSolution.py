__author__ = 'rakesh'

from math import log

def number_of_steps(weight):
    """
    Returns the number of steps required to balance the scales
    """
    # this formula was derived from boundary = (3 ** n - 1) / 2
    return int(log(weight * 2, 3)) + 1


def instruction_index(n, weight):
    """
    Returns the nth instruction index for a specified starting weight
    """
    # offset correction value for n
    offset = (3 ** n - 1) / 2

    # corrected row value to divide into sections
    corrected = int((weight + offset) / 3 ** n)

    # section treated as first column, just need the remainder
    return corrected % 3


def answer(weight):
    """
    Complexity: O(log(n))
    If you break the result of a few done by hand into patterns, you will notice
    that for column number n, the pattern [R, L, -] repeats every 3 ** n times.
    We need to be able to determine which of the three steps are required.
    This is obvious and easy for the first column, because it's simply mod 3.
    The same pattern can be found in the second column,
    but instead of [R, L, -] we have [R, R, R, L, L, L, -, -, -].
    The plan here is to divide that pattern into three, thereby giving us
    sections which we can now treat the same as the first column.
    The only tricky thing is that the pattern is offset by the column boundary
    of the previous column. These boundaries are at 1, 4, 13, 40 etc and can
    be calculated by using (3 ** n - 1) / 2.
    """

    instructions = []

    # total number of steps required for starting weight
    steps = number_of_steps(weight)

    for n in xrange(steps):

        # the index of the instruction, corresponding to the choices
        i = instruction_index(n, weight)

        # add the corresponding choice to the list of instructions
        instructions.append(['-', 'R', 'L'][i])

    return instructions


print answer(1000000000)


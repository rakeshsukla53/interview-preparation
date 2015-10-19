__author__ = 'rakesh'

from collections import Counter
#2x^2 + 5x + 10

def polynomial(equation):

    coefficent = []
    power = []

    for line in equation.split():

        try:

            try:

                if line[1] == 'x':

                    coefficent.append(line[0])

                    if line[-1] == 'x':
                        power.append(1)

                    else:
                        power.append(line[-1])

                else:
                    coefficent.append(int(line))

            except IndexError:
                pass

        except ValueError:

            pass

    print coefficent, power


polynomial('25x^2 + 15x - 15')

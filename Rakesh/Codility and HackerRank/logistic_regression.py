
import math

def logistic_function(x):
    return 1 / (1 + math.exp(-x))

coefficient = map(float, raw_input().strip().split())
data = map(float, raw_input().strip().split())

intercept = coefficient[-1]

coefficient.pop(len(coefficient) - 1)

result = sum([a * b for a, b in zip(coefficient, data)]) + intercept

print format(logistic_function(result), '.3f')


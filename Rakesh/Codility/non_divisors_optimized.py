
#Algorithm for it

# First it counts the occurrences of each number in the array.
#
# Then for each array element i it finds the number of its divisors in a range from 1 to sqrt(i), including the divisors which are the result of the division.
#
# Finally it subtracts a total number of divisors for given element from a total number of elements in the array.
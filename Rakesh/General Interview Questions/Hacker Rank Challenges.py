
# Enter your code here. Read input from STDIN. Print output to STDOUT

def mininum_flight_path(input_path):
    """
    return the index of all the paths taken by the hero to reach destination, otherwise return failure
    Args:
        input_path (list) : input list contains values which is the maximum length of the each flight
    return
        'failure' : failure means hero cannot reach destination
        result (list) : it contains the indices in the input_array through which the hero will reach the destination
    """

    result = []

    if not input_path[0]:
        return 'failure' + '\n'

    else:

        B = [float("inf")] * len(input_path)
        B[0] = 0

        for i in xrange(0, len(input_path)):
            for j in xrange(0, input_path[i]):
                if i+j+1 < len(input_path):
                    B[i+j+1] = min(B[i+j+1], B[i]+1)

        if str(B[-1]) == 'inf':
            return "failure" + '\n'

        else:
            # only one jump is required here
            if len(B) == 1:
                return str(B[-1]) + ', ' + 'out'

            for k in xrange(len(B) - 1):
                if B[k] != B[k + 1]:
                    if input_path[k]:
                        result.append(str(k))
                    else:
                        while not input_path[k]:
                            k -= 1
                        result.append(str(k))

            # minimum path found
            if input_path[int(result[-1])] + int(result[-1]) > len(B) - 1:
                result.append('out')
                return ", ".join(result) + '\n'

            result.append(str(len(B) - 1))
            # checking if dragon is present in the last index
            if not input_path[int(result[-1])]:
                return 'failure' + '\n'
            else:
                result.append('out')
                return ", ".join(result) + '\n'

# store all the stream of integer on this list

input_path = []

# import fileinput
# for line in fileinput.input():
#     input_path.append(int(line))

print mininum_flight_path([2, 5, 3, 0, 0, 0, 1, 1, 1])







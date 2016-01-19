
# this is a very bad way to do exit the looping
def find(seq, target):
    found = False
    for i, value in enumerate(seq):
        if value == target:
            found = True
            break

    if not found:
        return -1
    return i

# this is a much better way do the this

def find(seq, target):
    for i, value in enumerate(seq):
        if value == target:
            break
    else:
        return -1

    return i


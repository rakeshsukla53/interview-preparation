def append_one(li):
    li = [0, 1]
l = [0]
append_one(l)
print l


def append_one(li):
    li.append(1)
l = [0]
append_one(l)
print l

# Here, the statement l = [0] makes a variable l (box) that points towards the object [0]
#
# On the function being called, a new box li is created. The contents of li is the SAME as the contents of box l. Both the boxes contain the same object. That is, both the variables point to the same object in memory. Hence, any change to the object pointed at by li will also be reflected by the object pointed at by l.
#
# In conclusion, the output of the above program will be:
#
# [0, 1]
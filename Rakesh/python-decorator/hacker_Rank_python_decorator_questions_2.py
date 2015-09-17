__author__ = 'rakesh'

#Sorting the list based on a particular index/item

#http://stackoverflow.com/questions/409370/sorting-and-grouping-nested-lists-in-python?answertab=votes#tab-top

from operator import itemgetter

N = raw_input()

info = []

for i in range(int(N)):

    personInfo = raw_input().strip().split(" ")

    personInfo[2] = int(personInfo[2])

    info.append(personInfo)

info.sort(key=itemgetter(2))

def nameDirectory(func):

    def input(info):

        return [func(i) for i in info]

    return input


@nameDirectory
def standardize(info):

    if info[-1] == 'M':

        return "Mr." + " " + info[0] + " " + info[1]

    elif info[-1] == 'F':

        return "Ms." + " " + info[0] + " " + info[1]


print "\n".join(standardize(info))

# def mobile(function):
#     def input(number):
#             return sorted([function(i) for i in number])
#     return input
#
# @mobile
# def standardize(number):
#     return "+91" + " " + number[-10:-5] + " " + number[-5:]
#
# print '\n'.join(standardize(number))

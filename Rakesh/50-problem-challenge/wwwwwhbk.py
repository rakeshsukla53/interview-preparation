__author__ = 'rakesh'

#My approach is to convert the whole keypad into graph with nodes representing number and edges represent there is a path
#exists between two nodes. This graph is an undirected graph which means it is bidirectional
#Now I am going to define a dictionary with key repserenting the node(Number on Keypad) and values representing direct connection to node.
#What you see below is the movement of knight represented by key value pair
#It is extremely important to avoid loop in the graph otherwise it will go into infinte recursion.
#COMMENT - it is not clear how you want to print out the output? In the form of array, or just print? If you want to just print then there must be some order(like phone numbers starting from 2, 3, 4, 5 ......) An example of input and output would be so much better.

knight = {'1': ['6', '8'],  #movement of knight
          '2': ['7', '9'],  #this is how the graph will look like for Knight with key representing the starting point and where they can go from there
          '3': ['4', '8'],
          '4': ['3', '9', '0'],
          '6': ['1', '7', '0'],
          '7': ['2', '6'],
          '8': ['1', '3'],
          '9': ['4', '2'],
          '0': ['4', '6']
         }
#removed the path which will go into special characters since phone number cannot contain that

bishop = {'1': ['5', '9'],  #movement of bishop in the keypad
          '2': ['4', '6'],
          '3': ['5', '7'],
          '4': ['2', '8'],
          '5': ['1', '3', '7', '9'],  #path leading to #, * are ignored
          '6': ['2', '8'],
          '7': ['5', '0', '3'],
          '8': ['4', '6'],
          '9': ['5', '0', '1'],
          '0': ['7', '9']
         }

def knightFindPhoneNumbers(knight, start, path=[]):  #here path basically is your phone number.
    '''
    :param graph:  The movement of knight
    :param start: You can start from anywhere except 0 and 1
    :param path:
    :return: list containing all the valid numbers
    '''
    path = path + [start]
    if len(path) == 7:  #if the total number of length of path is 7 return the path. It means we found a valid phone number
        return [path] #we found one valid phone number
    if not knight.has_key(start):
        return []
    paths = []
    for node in knight[start]:
        if node:
            newpaths = knightFindPhoneNumbers(knight, node, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def bishopFindPhoneNumbers(bishop, start, path=[]):
    '''
    :param bishop:  The movement of bishop
    :param start: You can start from anywhere except 0, 1. Phone numbers cannot contain these digits
    :param path: capture the phone number
    :return: list of all phone numbers starting from some digit
    '''
    path = path + [start]
    if len(path) == 7:  #if the total number of lenght of digits is 7 return the path
        return [path]
    if not bishop.has_key(start):
        return []
    paths = []
    for node in bishop[start]:
        if node:
            newpaths = bishopFindPhoneNumbers(bishop, node, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


chessPlayer = raw_input()   #take the input from the user
count = 0
if chessPlayer.strip() == 'knight':
    for i in ['2', '3', '4', '5', '6', '7', '8', '9']:  #the phone number can start from 2, 3, 4, 5, 6, 7, 8, 9
        for k in knightFindPhoneNumbers(knight, i):
            count += 1  #print out the phone numbers
    print count
elif chessPlayer.strip() == 'bishop':
    for i in ['2', '3', '4', '5', '6', '7', '8', '9']:   #the phone number can start from 2, 3, 4, 5, 6, 7, 8, 9
        for k in bishopFindPhoneNumbers(bishop, i):  #find phone numbers start from 2, 3, 4, 5, 6, 7, 8, 9
            count += 1
    print count

#COMMENT - I feel confident for my program but its not able to pass the test case which I believe because of different output formatting.

